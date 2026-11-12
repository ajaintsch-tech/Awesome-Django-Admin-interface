# CLAUDE.md

Curated "awesome" list of Django admin themes, admin extensions and general Django resources.
The whole product is `README.md`; there is no application code.

## Structure
- `README.md` – the list. Admin sections first, then general Django libraries, then learning resources.
- `mkdocs.yml` – site config. CI copies `README.md`, `CONTRIBUTING.md` and `django.jpg` into `docs/` (git-ignored) and runs `mkdocs build --strict`.
- `.github/workflows/docs.yml` – builds on PRs, deploys `site/` to the `gh-pages` branch from `main`.
- `.github/workflows/link-check.yml` – lychee link check: monthly (opens an issue), on README changes (fails the run).
- `.lycheeignore` – URLs that block bots but work in a browser.

## Entry format (admin sections)
```
- **[name](https://github.com/owner/repo)** - One-line description. [D 5.2–6.1 · release 2026-11]
```
- `D x–y` = Django versions from the package's PyPI `Framework :: Django ::` classifiers; write `no versions listed` if none.
- `release YYYY-MM` = date of the latest PyPI release; use `last release` when older than ~2 years; `not on PyPI` if unpublished.
- Data comes from `https://pypi.org/pypi/<package>/json` (reachable from cloud sessions; most other hosts are not).
- Keep entries alphabetical only if the section already is; otherwise append.

## Rules
- Never delete or move an entry to "Older or Deprecated Projects" without the owner's approval – propose it in a report first.
- Badges and repo links point to `ajaintsch-tech/Awesome-Django-Admin-interface`, not the upstream `iamfoysal` repo.
- Verify a docs change with: `mkdir -p docs && cp README.md CONTRIBUTING.md django.jpg docs/ && mkdocs build --strict && rm -rf docs`.
