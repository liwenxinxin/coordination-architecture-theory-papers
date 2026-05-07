# docs/

This folder is the source for the GitHub Pages site that indexes the
trilogy of foundational papers for search engines (especially Google
Scholar and Perplexity-style retrieval systems).

## Layout

- `index.md` — auto-generated landing page. Lists the trilogy with
  full link metadata, and a single browse link to the corpus folder
  on GitHub.
- `papers/paper-{1,2,3}.html` — auto-generated landing pages for the
  trilogy with full Google Scholar `citation_*` metadata.
- `_config.yml` — Jekyll configuration.
- `robots.txt` — allows all crawlers; advertises the sitemap.
- `build_site.py` — regenerator. Re-run only when you publish a new
  trilogy paper (rare). Corpus papers do not require re-running.

## Adding new corpus papers

Drop new `.md` and `.pdf` files into
`core theory and corpus papers/md files/` and
`core theory and corpus papers/pdf files/`, then commit and push.

The index page does not list corpus papers individually — it links to
the corpus folder on GitHub, which auto-updates as you add files. No
script run required.

## Adding a new trilogy paper

1. Add the new `.md` and `.pdf` to `featured papers/md/` and
   `featured papers/pdf/`.
2. Open `docs/build_site.py` and add the new file's slug (filename
   without extension) to the comments and any logic that references
   the trilogy.
3. Run:
   ```bash
   python3 docs/build_site.py
   git add docs/
   git commit -m "Add trilogy paper N"
   git push
   ```

## One-time setup (already done if the site is live)

1. Push this folder to `main`.
2. In the repository on GitHub: **Settings -> Pages**.
3. Set **Source** to `Deploy from a branch`, **Branch** to `main`,
   **Folder** to `/docs`. Save.
4. Verify the site in [Google Search Console](https://search.google.com/search-console)
   and [Bing Webmaster Tools](https://www.bing.com/webmasters) using
   the verification files dropped into this folder.
5. Submit `sitemap.xml` in both consoles.
6. For Google Scholar: no submission needed — Scholar crawls
   discovered HTML pages with `citation_*` meta tags. The trilogy
   landing pages have those tags. Indexing typically takes 2–8 weeks.
