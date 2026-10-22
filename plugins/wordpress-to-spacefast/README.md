# wordpress-to-spacefast

Move a WordPress site from any host to Spacefast. Managed WordPress stays the place you write, a static Astro site built from a GitHub repo is the public front end, and DNS is cut over for one domain.

## What it does

Walks the move in phases and stops for an explicit yes before each structural change:

1. **Prerequisites** — a paid Spacefast team with managed WordPress, the `sf` CLI, and Node for local Astro builds
2. **Inventory** — a read-only count of posts, pages, media, comments, menus, forms, and permalinks
3. **Space and WordPress** — create the Space, check managed WordPress, and make it public only after a yes
4. **Content import** — custom post types as small plugins, then media, posts, pages, and comments, keeping the same slugs
5. **Astro front end** — a static build that recreates the old URL structure, checked on the `*.view.fast` preview before any DNS change
6. **Repo and auto-deploy** — commit the app, link the Spacefast GitHub App, and confirm the live version matches the commit
7. **Redirects and DNS** — `_redirects`, the exact DNS records, and a check that email records survive
8. **Publishing after the move** — prove one refresh path, because publishing a post does not rebuild the static site by itself

The old host is left untouched until you retire it.

## Install

See the [skillpack install steps](../../README.md#install).

Claude Code:

```
/plugin marketplace add p3ob7o/skillpack
/plugin install wordpress-to-spacefast@skillpack
```

The Claude Code command is `/wordpress-to-spacefast:wordpress-to-spacefast`.

Codex, after `codex plugin marketplace add p3ob7o/skillpack`:

```
codex plugin add wordpress-to-spacefast@skillpack
```

Cursor and Grok Bot: import `https://github.com/p3ob7o/skillpack` and install wordpress-to-spacefast, then invoke the `wordpress-to-spacefast` skill.

## Usage

Say you want to move a WordPress site. The skill asks where the site lives, which domain it should use, who manages DNS, and what to keep, then waits before changing anything structural.

## Structure

```
skills/
  wordpress-to-spacefast/
    SKILL.md    # The migration guide
```
