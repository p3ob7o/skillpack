# wordpress-to-spacefast

Version **1.0.0**. Move a WordPress site from any host to Spacefast: managed WordPress as a headless backend, a static Astro front end built from GitHub, and a DNS cutover.

## What it does

Walks the move in phases and waits for an explicit yes before each structural change. The old host stays untouched until you retire it.

1. **Prerequisites** — paid Spacefast team with managed WordPress, `sf` CLI, Node for local Astro builds
2. **Inventory** — read-only count of posts, pages, media, comments, menus, forms, and permalinks
3. **Space and WordPress** — create the Space, check managed WordPress, make it public only after a yes
4. **Content import** — custom post types as small plugins, then media, posts, pages, and comments, keeping the same slugs
5. **Astro front end** — static build that recreates the old URL structure; checked on the `*.view.fast` preview before any DNS change
6. **Repo and auto-deploy** — commit the app, link the Spacefast GitHub App, confirm the live version matches the commit
7. **Redirects and DNS** — `_redirects`, exact DNS records, check that email records survive
8. **Publishing after the move** — prove one refresh path; publishing a post does not rebuild the static site by itself

## Skills

| Skill | Claude Code | Codex / Cursor / Grok Bot |
|-------|-------------|---------------------------|
| `wordpress-to-spacefast` | `/wordpress-to-spacefast:wordpress-to-spacefast` | `/wordpress-to-spacefast` |

## Install

Shared marketplace steps: [skillpack install](../../README.md#install).

```
# Claude Code
/plugin install wordpress-to-spacefast@skillpack

# Codex (after marketplace add)
codex plugin add wordpress-to-spacefast@skillpack

# Cursor / Grok Bot
# Import https://github.com/p3ob7o/skillpack, then install wordpress-to-spacefast
```

## Usage

Say you want to move a WordPress site. The skill asks where the site lives, which domain it should use, who manages DNS, and what to keep, then waits before changing anything structural.

## Structure

```
skills/
  wordpress-to-spacefast/
    SKILL.md
```
