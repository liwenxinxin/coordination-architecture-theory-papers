#!/usr/bin/env python3
"""
build_site.py — Auto-generates the GitHub Pages site for the
coordination-architecture-theory-papers repository.

Walks the parent directory, extracts titles and dates from the markdown
versions of each paper, and writes:

  - docs/index.md            (the landing page listing every paper)
  - docs/papers/paper-N.html (Scholar-friendly landing pages for the trilogy)

Re-run this script whenever you add new papers. No copy-pasting required.

Usage (from repo root):
    python3 docs/build_site.py
"""

from __future__ import annotations
import os
import re
import shutil
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration — edit these if you change repo structure or move things
# ---------------------------------------------------------------------------

REPO_OWNER  = "liwenxinxin"
REPO_NAME   = "coordination-architecture-theory-papers"
SITE_TITLE  = "Coordination Architecture Theory Papers"
SITE_DESC   = ("Research papers on the Coordination Knowledge Substrate (CKS) "
               "pattern — a human-governed, AI-mediated coordination "
               "architecture. By Wenxin Li.")
AUTHOR_NAME = "Wenxin Li"
AUTHOR_ORCID = "0009-0004-8065-3235"

# Paths are computed relative to the repo root (parent of docs/).
REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR  = REPO_ROOT / "docs"

FEATURED_MD_DIR  = REPO_ROOT / "featured papers" / "md"
FEATURED_PDF_DIR = REPO_ROOT / "featured papers" / "pdf"

# The corpus is no longer enumerated on the index page. Instead, the index
# links to the GitHub folder containing the corpus PDFs. Browsers and
# crawlers can both navigate that folder; we don't have to maintain a list
# that grows every time a new corpus paper is added.
CORPUS_FOLDER_URL = (
    f"https://github.com/{REPO_OWNER}/{REPO_NAME}/tree/main/"
    "core%20theory%20and%20corpus%20papers/pdf%20files"
)

# ---------------------------------------------------------------------------
# Data extraction
# ---------------------------------------------------------------------------

@dataclass
class Paper:
    slug: str            # filename without .md
    title: str
    date: str            # raw date string as found in the file
    md_path: Path        # absolute path to the .md
    pdf_path: Path | None  # absolute path to the .pdf, if present

    @property
    def md_repo_relpath(self) -> str:
        return str(self.md_path.relative_to(REPO_ROOT)).replace(os.sep, "/")

    @property
    def pdf_repo_relpath(self) -> str | None:
        if self.pdf_path is None:
            return None
        return str(self.pdf_path.relative_to(REPO_ROOT)).replace(os.sep, "/")

    def github_blob_url(self, kind: str) -> str:
        rel = self.md_repo_relpath if kind == "md" else self.pdf_repo_relpath
        if rel is None:
            return ""
        return (f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/main/"
                f"{urllib.parse.quote(rel)}")

    def github_raw_url(self, kind: str) -> str:
        rel = self.md_repo_relpath if kind == "md" else self.pdf_repo_relpath
        if rel is None:
            return ""
        return (f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/"
                f"main/{urllib.parse.quote(rel)}")


TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
DATE_RE_BOLD  = re.compile(r"^\*\*Date:\*\*\s+(.+?)\s*$", re.MULTILINE)
DATE_RE_LOOSE = re.compile(
    r"^(January|February|March|April|May|June|July|August|"
    r"September|October|November|December)\s+\d{4}\s*$",
    re.MULTILINE,
)


def extract_title_and_date(md_path: Path) -> tuple[str, str]:
    """Return (title, date) extracted from the first H1 and the date line."""
    text = md_path.read_text(encoding="utf-8", errors="replace")
    head = text[:4000]  # first ~4KB is plenty
    title_match = TITLE_RE.search(head)
    title = title_match.group(1).strip() if title_match else md_path.stem

    date = ""
    m = DATE_RE_BOLD.search(head)
    if m:
        date = m.group(1).strip()
    else:
        m = DATE_RE_LOOSE.search(head)
        if m:
            date = m.group(0).strip()
    return title, date


def load_papers(md_dir: Path, pdf_dir: Path) -> list[Paper]:
    papers: list[Paper] = []
    for md in sorted(md_dir.glob("*.md")):
        slug = md.stem
        pdf = pdf_dir / f"{slug}.pdf"
        title, date = extract_title_and_date(md)
        papers.append(Paper(
            slug=slug,
            title=title,
            date=date,
            md_path=md,
            pdf_path=pdf if pdf.exists() else None,
        ))
    return papers


# ---------------------------------------------------------------------------
# Output: index.md
# ---------------------------------------------------------------------------


def write_index(trilogy: list[Paper]) -> None:
    lines: list[str] = []
    lines.append("---")
    lines.append("layout: default")
    lines.append(f'title: "{SITE_TITLE}"')
    lines.append(f'description: "{SITE_DESC}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {SITE_TITLE}")
    lines.append("")
    lines.append(f"*By {AUTHOR_NAME} (Independent Researcher) — "
                 f"ORCID [{AUTHOR_ORCID}](https://orcid.org/{AUTHOR_ORCID})*")
    lines.append("")
    lines.append(SITE_DESC)
    lines.append("")
    lines.append("All papers are released under "
                 "[Creative Commons Attribution 4.0 International "
                 "(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Featured trilogy — these get dedicated landing pages with citation meta.
    lines.append("## Foundational Trilogy")
    lines.append("")
    lines.append("The three core theory papers introducing and extending the "
                 "Coordination Knowledge Substrate (CKS) pattern. Each has a "
                 "dedicated landing page with citation metadata.")
    lines.append("")
    for i, p in enumerate(trilogy, start=1):
        landing = f"papers/paper-{i}.html"
        md_url  = p.github_blob_url("md")
        pdf_url = p.github_blob_url("pdf") if p.pdf_path else ""
        links = [f"[Landing page]({landing})"]
        if pdf_url:
            links.append(f"[PDF]({pdf_url})")
        if md_url:
            links.append(f"[Markdown]({md_url})")
        date_part = f"  \n  *{p.date}*" if p.date else ""
        lines.append(f"- **{p.title}**{date_part}")
        lines.append("  \n  " + " · ".join(links))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Corpus — single browse link, no enumeration, no count.
    lines.append("## Corpus Papers")
    lines.append("")
    lines.append("Standalone deep-dive treatments — one paper per "
                 "architectural commitment, integrating frame, sub-claim, "
                 "composition, and anti-pattern in the CKS pattern. Each "
                 "paper formalizes one aspect of the framework in "
                 "operational depth.")
    lines.append("")
    lines.append(f"[Browse the full corpus on GitHub →]({CORPUS_FOLDER_URL})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Source Repository")
    lines.append("")
    lines.append(f"All source files (Markdown and PDF) are versioned in the "
                 f"[GitHub repository]"
                 f"(https://github.com/{REPO_OWNER}/{REPO_NAME}).")

    (DOCS_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Output: per-paper landing pages for the trilogy (Scholar metadata)
# ---------------------------------------------------------------------------

LANDING_TEMPLATE = """\
---
layout: null
---
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} — {site_title}</title>
<meta name="description" content="{description}">

<!-- Google Scholar citation metadata -->
<meta name="citation_title" content="{title}">
<meta name="citation_author" content="{author}">
<meta name="citation_publication_date" content="{date}">
<meta name="citation_pdf_url" content="{pdf_url}">
<meta name="citation_language" content="en">
<meta name="citation_keywords" content="coordination knowledge substrate; CKS; AI architecture; human-governed AI; coordination architecture; AI mediator; substrate pattern">

<!-- Dublin Core -->
<meta name="DC.title" content="{title}">
<meta name="DC.creator" content="{author}">
<meta name="DC.date" content="{date}">
<meta name="DC.type" content="Text.Article">
<meta name="DC.format" content="application/pdf">
<meta name="DC.identifier" content="{pdf_url}">
<meta name="DC.rights" content="Creative Commons Attribution 4.0 International (CC BY 4.0)">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{landing_url}">

<link rel="canonical" href="{landing_url}">

<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          sans-serif; max-width: 760px; margin: 2rem auto; padding: 0 1rem;
          line-height: 1.55; color: #222; }}
  h1 {{ font-size: 1.6rem; line-height: 1.3; }}
  .meta {{ color: #555; font-size: 0.95rem; margin-bottom: 1.5rem; }}
  .links a {{ display: inline-block; margin-right: 1rem; }}
  hr {{ border: 0; border-top: 1px solid #ddd; margin: 2rem 0; }}
  .abstract {{ background: #fafafa; padding: 1rem 1.25rem;
               border-left: 3px solid #888; }}
</style>
</head>
<body>

<p><a href="../">&larr; Back to all papers</a></p>

<h1>{title}</h1>

<p class="meta">
  <strong>{author}</strong> &middot; Independent Researcher<br>
  ORCID: <a href="https://orcid.org/{orcid}">{orcid}</a><br>
  {date} &middot; CC BY 4.0
</p>

<p class="links">
  <a href="{pdf_url}"><strong>Download PDF</strong></a>
  <a href="{md_url}">View Markdown source</a>
</p>

<hr>

<div class="abstract">
{abstract_html}
</div>

<hr>

<p>This paper is part of a trilogy on the Coordination Knowledge Substrate
(CKS) pattern. See the <a href="../">main paper index</a> for the full
corpus, including foundational concept papers and operational deep-dive
treatments.</p>

<p><strong>Cite as:</strong><br>
Li, W. ({year}). <em>{title}</em>. Coordination Architecture Theory Papers.
{landing_url}</p>

</body>
</html>
"""


def extract_abstract_html(md_path: Path) -> str:
    """Pull the Abstract section out of the markdown and convert it to
    minimal HTML paragraphs. We keep this dependency-free."""
    text = md_path.read_text(encoding="utf-8", errors="replace")
    # Find "## Abstract" header, take everything until the next "## " header
    m = re.search(r"^##\s+Abstract\s*$", text, re.MULTILINE)
    if not m:
        return "<p><em>Abstract not found in source markdown.</em></p>"
    start = m.end()
    next_h = re.search(r"^##\s+", text[start:], re.MULTILINE)
    body = text[start:start + next_h.start()] if next_h else text[start:]
    body = body.strip()
    # Trim leading/trailing horizontal rules
    body = re.sub(r"^---\s*", "", body).strip()
    body = re.sub(r"\s*---$", "", body).strip()
    # Split into paragraphs and minimally HTML-encode
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    out: list[str] = []
    for p in paras:
        # Bold + italics passthrough is fine; just escape bare angle brackets
        p_html = p.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        # Restore basic markdown emphasis -> HTML
        p_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p_html)
        p_html = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", p_html)
        out.append(f"<p>{p_html}</p>")
    return "\n".join(out)


def first_sentence(text_html: str, max_chars: int = 220) -> str:
    plain = re.sub(r"<[^>]+>", "", text_html).strip()
    plain = plain.replace('"', "&quot;")
    if len(plain) <= max_chars:
        return plain
    cut = plain[:max_chars]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


def write_trilogy_landing_pages(featured: list[Paper]) -> None:
    pages_dir = DOCS_DIR / "papers"
    pages_dir.mkdir(parents=True, exist_ok=True)
    base_url = f"https://{REPO_OWNER}.github.io/{REPO_NAME}"
    for i, p in enumerate(featured, start=1):
        abstract_html = extract_abstract_html(p.md_path)
        description   = first_sentence(abstract_html)
        # Year extraction (best-effort): last 4-digit run in the date string
        year_match = re.search(r"(20\d{2})", p.date)
        year = year_match.group(1) if year_match else ""
        pdf_url = p.github_raw_url("pdf") if p.pdf_path else ""
        md_url  = p.github_blob_url("md")
        landing_url = f"{base_url}/papers/paper-{i}.html"

        html = LANDING_TEMPLATE.format(
            title=p.title,
            site_title=SITE_TITLE,
            description=description,
            author=AUTHOR_NAME,
            orcid=AUTHOR_ORCID,
            date=p.date,
            year=year,
            pdf_url=pdf_url,
            md_url=md_url,
            landing_url=landing_url,
            abstract_html=abstract_html,
        )
        (pages_dir / f"paper-{i}.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# Output: Jekyll config and helper files
# ---------------------------------------------------------------------------

def write_jekyll_config() -> None:
    # Jekyll concatenates url + baseurl + page path to build absolute URLs
    # (in the sitemap, canonical tags, etc.), so `url` must be host-only.
    # Putting the repo name in both produces doubled paths.
    site_host = f"https://{REPO_OWNER}.github.io"
    config = f"""\
# Auto-generated by docs/build_site.py — edit and re-run if needed.
title: "{SITE_TITLE}"
description: "{SITE_DESC}"
author: "{AUTHOR_NAME}"
url: "{site_host}"
baseurl: "/{REPO_NAME}"

theme: minima

plugins:
  - jekyll-sitemap
  - jekyll-seo-tag

# Don't process the build script as a page.
exclude:
  - build_site.py
  - README.md
"""
    (DOCS_DIR / "_config.yml").write_text(config, encoding="utf-8")


def write_robots() -> None:
    base_url = f"https://{REPO_OWNER}.github.io/{REPO_NAME}"
    body = f"""\
User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""
    (DOCS_DIR / "robots.txt").write_text(body, encoding="utf-8")


def write_readme() -> None:
    body = """\
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
"""
    (DOCS_DIR / "README.md").write_text(body, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Repo root: {REPO_ROOT}")
    trilogy = load_papers(FEATURED_MD_DIR, FEATURED_PDF_DIR)
    print(f"Trilogy papers found: {len(trilogy)}")

    write_index(trilogy)
    print("Wrote docs/index.md")

    write_trilogy_landing_pages(trilogy)
    print(f"Wrote {len(trilogy)} trilogy landing pages")

    write_jekyll_config()
    print("Wrote docs/_config.yml")

    write_robots()
    print("Wrote docs/robots.txt")

    write_readme()
    print("Wrote docs/README.md")

    print("\nDone. Review docs/, commit, and push.")


if __name__ == "__main__":
    main()
