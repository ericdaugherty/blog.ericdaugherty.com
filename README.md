# blog.ericdaugherty.com

Source for [blog.ericdaugherty.com](https://blog.ericdaugherty.com), a Hugo-powered blog hosted on GitHub Pages.

## Tech stack

- [Hugo](https://gohugo.io/) Extended **0.157.0**
- Deployed to GitHub Pages via [.github/workflows/hugo.yml](.github/workflows/hugo.yml)
- Custom domain configured via [static/CNAME](static/CNAME)

## Local development

Install [Hugo Extended 0.157.0](https://gohugo.io/installation/), then from the repo root:

```bash
./serve.sh
```

This runs `hugo server --disableFastRender -D` (drafts enabled) and serves the site at <http://localhost:1313>.

## Creating a new post

```bash
./newpost.sh my-post-slug
```

This creates `content/posts/YYYY-MM-DD-my-post-slug.md` from [archetypes/default.md](archetypes/default.md) and sets the post title to Title Case. Edit the frontmatter and body, then `git push` to publish.

## Project layout

- [content/posts/](content/posts/) — blog posts (many migrated from Blogger)
- [layouts/](layouts/) — custom Hugo templates, including [_default/rss.xml](layouts/_default/rss.xml) for full-content RSS
- [assets/css/main.css](assets/css/main.css) — site styles (minified + fingerprinted at build)
- [static/](static/) — `CNAME`, favicon, migrated images, legacy feed redirects
- [archetypes/default.md](archetypes/default.md) — template used by `newpost.sh`
- [scripts/import_blogger.py](scripts/import_blogger.py) — one-time Blogger import script, kept for reference
- [hugo.toml](hugo.toml) — site config

## Deployment

Pushes to `main` trigger [.github/workflows/hugo.yml](.github/workflows/hugo.yml), which downloads the pinned Hugo version, runs `hugo build --gc`, and deploys the `public/` output to GitHub Pages.

## Permalinks & feeds

- Posts: `/:year/:month/:slug.html`
- RSS: `/index.xml` (full post content via the custom RSS template)
