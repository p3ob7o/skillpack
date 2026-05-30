# PPT conversion — extract content from a PowerPoint file

When the user wants to convert an existing `.ppt` or `.pptx` to a deck, extract the content first (with `python-pptx`), confirm the structure with the user, then generate slides using the Automattic layouts.

## Extraction script

```python
from pptx import Presentation
import os, json

def extract_pptx(file_path, output_dir):
    """
    Extract slides, text, images, and speaker notes from a PowerPoint file.
    Images are written to {output_dir}/assets/ (referenced by relative path
    in the returned structure — these can later be uploaded somewhere and
    referenced by URL in the final single-file deck, since the deck output
    inlines everything except remote images).
    """
    prs = Presentation(file_path)
    assets_dir = os.path.join(output_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    slides = []
    for n, slide in enumerate(prs.slides, start=1):
        data = {"number": n, "title": "", "content": [], "images": [], "notes": ""}

        for shape in slide.shapes:
            if shape.has_text_frame:
                if shape == slide.shapes.title:
                    data["title"] = shape.text
                else:
                    data["content"].append({"type": "text", "content": shape.text})

            if shape.shape_type == 13:  # Picture
                img = shape.image
                ext = img.ext
                name = f"slide{n}_img{len(data['images']) + 1}.{ext}"
                with open(os.path.join(assets_dir, name), "wb") as f:
                    f.write(img.blob)
                data["images"].append({"path": f"assets/{name}"})

        if slide.has_notes_slide:
            data["notes"] = slide.notes_slide.notes_text_frame.text

        slides.append(data)

    return slides
```

Install: `pip install python-pptx`.

## Workflow

1. **Run the extractor.** Write `extract.py` (above), run it pointed at the source PPT, save the JSON output to a temp file. Don't store extracted images in the skill's working dir — write them to a sibling `assets/` folder next to the eventual deck.

2. **Summarize the structure back to the user**, asking them to confirm before proceeding:

   ```
   I've extracted the following from your PowerPoint:

   Slide 1: <title>
     • <first 60 chars of content>
     • Images: <count>
     • Speaker notes: <yes/no>

   Slide 2: ...
   ```

3. **Map each PPT slide to an Automattic layout.** Most extracted slides will fall into one of these buckets:

   | PPT pattern | Automattic layout |
   |---|---|
   | Title slide with author info | Layout 1 (Cover) |
   | Section title alone | Layout 14 (white divider) or Layout 5 (black divider with numeral) |
   | Bulleted content slide | Layout 8 (Bulleted list) |
   | Stats / KPIs | Layout 6 (Numeric layout) |
   | Comparison table | Layout 9 (Table) |
   | Quote slide | Layout 10 (Pull quote) |
   | 3-column comparison | Layout 11 (Three columns) |
   | Body + screenshot | Layout 12 (Long-form with images) |
   | Numbered steps (1, 2, 3) | Layout 13 (Numbered data 1-3) |
   | "Thank you" / closing | Layout 15 (Closing) |

   If a PPT slide doesn't fit any layout cleanly, propose splitting it or simplifying the content to fit Automattic's density limits (max 6 bullets, max 3 metrics per row, etc.).

4. **Handle images.** The extracted images live in a sibling `assets/` folder. The Automattic deck system uses `.image-slot` placeholders by default (solid blue or grey rectangles), but for a converted deck you'll usually want real images.

   Two paths:
   - **Reference by URL.** If the user uploads images somewhere (CDN, S3, GitHub raw), reference them with `<img src="https://...">` inside the deck — the single-file constraint allows external image URLs.
   - **Inline as base64 data URIs.** For images that must travel with the deck, convert each to a `data:image/png;base64,...` URI and use it as `src`. Adds bytes but preserves the single-file guarantee. Recommend only for small images (<50KB each).

5. **Carry speaker notes over.** PowerPoint's `slide.notes_slide.notes_text_frame.text` returns plain text. Split it into bullets (one per sentence, or use the user's existing line breaks), then drop into the `notes` array of the corresponding `speaker-notes` entry. Estimate `seconds` per slide as `max(15, len(notes_text) / 12)` — roughly 12 chars per spoken second.

6. **Generate the final deck** using the standard workflow in SKILL.md.

## Caveats

- **Layout fidelity is not the goal.** The point of conversion is to bring the content into the Automattic deck style, not to recreate the source PPT's visual layout. Resist the temptation to add extra columns, accent colors, or layouts to "match the original."
- **Reject dense slides.** If a PPT slide has 12 bullet points or 6 columns, split it. Density limits are non-negotiable — they're what makes the style work.
- **Animations don't carry over.** PowerPoint animations are dropped silently. The Automattic style has no animations by design.
