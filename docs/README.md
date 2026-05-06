# docs/

This folder is the source for the GitHub Pages site that indexes every
paper in this repository for search engines (especially Google Scholar
and Perplexity-style retrieval systems).

## Layout

- `index.md` — auto-generated landing page listing every paper.
- `papers/paper-{1,2,3}.html` — auto-generated landing pages for the
  trilogy with full Google Scholar `citation_*` metadata.
- `_config.yml` — Jekyll configuration.
- `robots.txt` — allows all crawlers; advertises the sitemap.
- `build_site.py` — regenerator. Re-run after adding new papers.

## Regenerating after adding papers

```bash
python3 docs/build_site.py
git add docs/
git commit -m "Rebuild docs index"
git push
```

## One-time setup

1. Push this folder to `main`.
2. In the repository on GitHub: **Settings -> Pages**.
3. Set **Source** to `Deploy from a branch`, **Branch** to `main`, **Folder** to `/docs`. Save.
4. Wait ~1 minute. The site will be live at
   `https://liwenxinxin.github.io/coordination-architecture-theory-papers/`.
5. Verify the site in [Google Search Console](https://search.google.com/search-console)
   using the HTML meta tag method (paste it into `_config.yml` under a
   `google_site_verification:` key, or drop the verification HTML file
   into `docs/`).
6. Submit the sitemap URL `…/sitemap.xml` in Search Console.
7. For Google Scholar specifically: no submission needed — Scholar
   crawls discovered HTML pages with `citation_*` meta tags. The trilogy
   landing pages have those tags. Indexing typically takes 2–8 weeks.
