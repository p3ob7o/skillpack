---
name: wordpress-to-spacefast
description: Use when someone wants to move a WordPress site from any host to Spacefast, with Spacefast's managed WordPress as a headless backend, a static Astro front end deployed from GitHub, and a DNS cutover for one domain. Covers inventory, content import, the Astro build, redirects, DNS, and how to publish after the move.
license: GPL-2.0
---

# Move a WordPress site to Spacefast (headless WordPress + Astro)

In this skill, "I" and "me" mean the user who owns the site. Their yes is needed at every **[ASK ME]** gate.

Use this skill to migrate the user's WordPress site to Spacefast. Spacefast's managed WordPress becomes a **headless backend**
(I keep writing in wp-admin), and a **static Astro site** built from a GitHub repo is the public front end.
Work carefully, in the phases below, and stop at every **[ASK ME]** gate for my explicit yes.

## Start by asking the user
Before doing anything else, ask me these questions, one short message at a time or as a single list,
and wait for my answers. Don't guess. If I don't know an answer, help me find it (for example, by reading
the site's public REST API or DNS). Then repeat my answers back as a short summary and wait for my go-ahead.
1. What's the address of the site you're moving, and who hosts it today?
2. Which domain should the new site live on, and should the main address be with or without `www`?
3. Who manages that domain's DNS today, and does it also carry email (MX records) or other services?
4. Do you already have a Spacefast team on a paid plan with managed content turned on? What should the new Space be called?
5. Which GitHub account or organization should hold the front-end repo, and what should the repo be called? (You'll create it.)
6. Does the site use any custom post types or custom fields we need to keep?
7. Should existing comments come along, and should new comments stay open?
8. Are there any forms or a newsletter signup? If so, which service should they go to, or should we drop them?
9. Is there anything about the current design or behaviour you want to change, or should the new site match the old one?

## Ground rules
1. **Don't touch the old host.** It's the content source and the fallback until I retire it myself.
2. **Preview first.** Build and check everything on the Space's `*.view.fast` preview URL before any DNS change.
   Structural changes go live only after my yes.
3. **Keep every URL.** Same slugs, same permalink structure. Anything that has to move gets a 301 in `_redirects`.
4. **Prove it.** After every publish, report the version number and the URL you checked. No "should work".
5. **Secrets stay secret.** Never print or commit API keys, tokens, sign-in links or DNS verification values.
6. **I handle DNS, domains, plans, GitHub and billing.** You prepare exact steps and verify afterwards.
7. **Never delete content, a site or a Space**, and never publish a post, without my explicit yes.

## Phase 0: Prerequisites (check each and tell me what's missing)
- A Spacefast team on a paid plan with **managed content (managed WordPress)** turned on. If it's off, nothing
  else works, so check this first.
- The `sf` CLI installed (`sf --version`) and signed in with a team API key that I create and hand over securely.
- Node ≥ 22.12 for local Astro builds (recent Astro and `@spacefast/astro` refuse older versions).
- Read access to the old site: its public REST API (`/wp-json/wp/v2/...`) is usually enough. Use SSH or wp-cli if the host offers it.

## Phase 1: Inventory the old site (read-only)
Count and list: posts, pages, custom post types, categories, tags, media (count and total size), comments,
menus, forms, the permalink structure, and any existing redirects. Note anything the theme does that a static site
must reproduce (archives, pagination, feeds, search, related posts). Save the inventory as JSON plus a short summary for me.
**[ASK ME]** what to keep, what to drop, and whether comments come along.

## Phase 2: Create the Space and its WordPress
1. Create the Space. Keep it private behind a coming-soon page while you build.
2. Check managed WordPress: list plugins and post types, and test a media upload.
   - Managed wp-admin hides **Settings** and **Plugins**, and file mods are disabled. Install plugins with
     `sf wp plugin install <zip> --activate`, and don't plan anything that needs a plugin settings screen.
   - If uploads fail with "Unable to create directory", storage isn't provisioned yet. It usually works after the
     Space's first real publish.
3. A static front end reads WordPress anonymously, so the Space must be **public** before the Astro build can fetch.
   **[ASK ME]** before making it public, then check that `curl -s -o /dev/null -w '%{http_code}' https://<space>.view.fast/wp-json/` returns `200`.

## Phase 3: Content model and import
1. Recreate the content model **before** importing. Package each custom post type (and its taxonomy) as a small
   regular plugin with `show_in_rest: true`. Keep its source in the repo under `wordpress/plugins/<name>/`, and install it via `sf wp`.
2. Create categories and tags first and keep an old→new ID map.
3. Import through the Space's WordPress REST API, in this order: media (multipart `POST /wp/v2/media`),
   then posts, pages and CPT items with their featured media, terms, dates, authors and meta, then comments.
   Rewrite media URLs inside content to the new media.
4. **Keep the same slugs.** Check each one with `GET /wp/v2/<type>?slug=<slug>`. Check that terms really stuck,
   because REST term assignment can silently fail.
5. Do a small trial batch first, show me the result, then run the rest. Make the import resumable, with a log of old ID → new ID.
6. Back off and retry on 429/5xx. Bursts get rate-limited.

## Phase 4: The Astro front end
1. Static Astro (`output: "static"`, `trailingSlash: "always"`, the `@spacefast/astro` integration), with
   `sf.jsonc` → `{"build": {"buildCommand": "npm run build", "outputDirectory": "dist"}}`.
2. Fetch content from WordPress at build time (a pre-build fetch script, or Astro's own data loading), with retry
   and backoff. Fail loudly instead of publishing an empty site.
3. Recreate the URL structure exactly: `/<slug>/` singles, page paths, `/category/.../`, `/tag/.../`, `/page/N/`
   pagination, date archives if the old site had them, RSS feeds at `/feed/`, `robots.txt` and a sitemap.
4. **Resolve internal links by path, not by host.** WordPress rewrites stored links to whatever domain is primary,
   so the build should map any internal link (old domain, Spacefast preview domain, `www`) to the right page.
   Leave `/wp-content/` media URLs alone.
5. Port the design: reuse the old theme's CSS and fonts (self-host them), and write the markup as plain static HTML.
   Don't invent copy. Take it only from the old site.
6. Forms and comments: a static site has no server. Either wire them to a real external endpoint and test a real
   submission, or show comments read-only and close new ones. **[ASK ME]** which.
7. Build locally, publish to the preview (`sf publish ./dist --prebuilt --space <space> --wait`), and check it
   page by page against the old site. Send me screenshots of the home page, one post, one archive and the 404 page.

## Phase 5: Repo and auto-deploy
1. Commit the whole app plus the WordPress plugins to `<owner>/<repo>`. Exclude `node_modules`, `dist`, `.astro`,
   `.env*`, local Spacefast state and any credentials. Run a secret scan before the first push.
2. **[ASK ME]** to install the Spacefast GitHub App **on the same Spacefast team** as the Space and to approve linking the repo
   (a team API key can't link GitHub, so I'll approve a device sign-in).
3. Push to `main`, let Spacefast build, and check that the live version matches the commit you pushed. Check this after
   every build: the repo sync can lag or get stuck, so run `sf git sync` before `sf git build` if it does.

## Phase 6: Redirects, then DNS cutover
1. Before DNS changes, list every redirect we need (old permalinks, renamed slugs, feeds, author and date archives,
   `www` → apex) in `public/_redirects`. Mind the platform's rule limit, and note that host-specific rules only work once
   the domain is attached to the Space.
2. Prepare the exact DNS steps for me: add the domain to the Space (`sf domains add <domain> --space <space>`) and
   copy the records Spacefast prints. Usually that's a TXT ownership record plus either A/AAAA records or a switch
   to Spacefast's nameservers. **Recreate every non-web record** (MX for email, SPF/DKIM/DMARC, other verification TXTs)
   before any nameserver switch, or email breaks.
3. **[ASK ME]** I make the DNS change. Then check from several resolvers (`dig @1.1.1.1`, `dig @8.8.8.8`) and load the
   apex **and** `www` over HTTPS. A CNAME on `www` can block TXT verification, and some registrar panels save `@` literally.
   Certificates only issue once DNS points at Spacefast, so allow minutes to hours.
4. Once the domain is verified, **publish again** so the host-specific redirects apply, then test a sample of old URLs for their 301s.
5. Turn on indexing: remove `noindex`, and check `robots.txt` and the sitemap on the real domain.

## Phase 7: Publishing after the move
Managed WordPress has no "on publish" hook, so publishing a post does **not** rebuild the static site by itself.
Set up and **prove** one refresh path, then tell me which you picked:
- simplest: I tell you, and you trigger a build (`sf git build`, a push to `main`, or Spacefast's build-trigger API);
- or a scheduled job that checks WordPress's latest `modified_gmt` and rebuilds only when it changed.
Test it with a harmless edit and revert it.

## Verification checklist (report each item with evidence)
- [ ] `/wp-json/` returns 200 anonymously, and media URLs return 200.
- [ ] Every migrated slug resolves on the new site, archives list every item, and the counts match the inventory.
- [ ] Old URLs (sample from the inventory) 301 to the right place. No internal link points at the old host or preview domain.
- [ ] Apex and `www` load over HTTPS with a valid certificate, and `www` redirects to the apex (or the other way round).
- [ ] Email still works (MX, SPF, DKIM and DMARC are present).
- [ ] The repo's `main` matches the live version, and a push rebuilds the site.
- [ ] Feeds, sitemap and robots.txt are live, and the site is indexable.
- [ ] Forms (if any) work on a real submission.
- [ ] Publishing a new post reaches the live site via the chosen refresh path.

## Rollback
Spacefast versions are immutable, so you can roll the front end back to an earlier version. The old host stays intact,
so rolling DNS back restores the old site. Code history lives in the repo.
