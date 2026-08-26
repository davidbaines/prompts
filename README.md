# Prompt Library

A public catalogue of AI prompts. A person reviews new prompts before any are added.
Each prompt is a Markdown file under [`prompts/`](prompts/), containing metadata and version history.

---

## Finding a prompt

Three ways, roughly fastest-first:

1. **Search** the repo (the search box on the code host, or `grep` locally) for a
   keyword, tag, or phrase.
2. **Browse** the `prompts/` folder — filenames are descriptive slugs.
3. **Filter by tag** — every prompt lists `tags:` in its metadata; search e.g.
   `tags: summarizing` to see everything in a category.

Each file tells you at a glance what it's for (`purpose`), which models it was
tuned on (`models`), whether it's been reviewed (`status`), and how it's changed
(the Changelog section + Git history).

---

## Adding or changing a prompt

1. Copy [`templates/TEMPLATE.md`](templates/TEMPLATE.md) to a new file in
   `prompts/` named after its `id`, e.g. `prompts/weekly-status-summary.md`.
2. Fill in every metadata field and write the prompt using the **placeholder
   convention** (below).
3. Run through the **PII & proprietary-data checklist** (below) yourself.
4. Run `python scripts/validate.py` (needs Python 3 and PyYAML) and fix any
   errors, then `python scripts/update_index.py` to regenerate `INDEX.md`.
5. Open a pull request that includes the regenerated `INDEX.md`. A curator
   reviews it — this review is our compliance gate — and merges it. On merge,
   `status` becomes `reviewed`.

To change an existing prompt: edit the file, bump the `version` field, add a
Changelog line, and open a PR the same way. The old version is never lost — it
lives in the Git history.

---

## Metadata schema

Every prompt file opens with this YAML block. Fill every required field; the
optional fields matter mainly for prompts that can run unattended.

| Field     | Required | What it's for                                                        |
|-----------|----------|----------------------------------------------------------------------|
| `title`   | yes      | Short human-readable name.                                           |
| `id`      | yes      | Stable lowercase slug. Set once, never change it — other files and links may reference it. |
| `purpose` | yes      | One sentence: what it does and when to use it. This is the line people scan. |
| `tags`    | yes      | Discovery keywords. Reuse existing tags where you can.               |
| `models`  | yes      | Which model(s) it was tuned on, so users know what it's been tested against. |
| `author`  | yes      | Who contributed it.                                                  |
| `source`  | yes      | `original`, or where it was adapted from — this is how we tell prompts we wrote apart from ones we adopted. |
| `version` | yes      | Integer. Bump on every meaningful change.                           |
| `created` | yes      | `YYYY-MM-DD`.                                                        |
| `updated` | yes      | `YYYY-MM-DD` of the last change.                                     |
| `status`  | yes      | `draft` (proposed), `reviewed` (merged after review — the normal state), `proven` (granted by the curation crew as reliably useful), or `deprecated` (kept for history, don't use). |
| `automation` | no    | `interactive`, `scheduled`, `triggered`, or `scheduled-or-triggered`. Defaults to `interactive`. |
| `triggers`   | no    | List from `cron`, `email`, `slack`, `calendar`. Empty for interactive prompts. |
| `rank`       | no    | Integer. Used only by the initial curated set for ordering.          |

Consistent tags and slugs are what keep this a library rather than a pile. When
in doubt, match an existing prompt's style.

---

## The placeholder convention

**Prompts in this repo never contain real names, numbers, clients, internal
figures, or documents.** Anything situation-specific is written as a
`[SQUARE_BRACKET]` placeholder and filled in privately at use time:

```text
Summarise [RAW_NOTES] for [STAKEHOLDER] in [OUTPUT_FORMAT].
```

not

```text
Summarise the attached Q3 revenue figures for Jane Okafor in a one-pager.
```

This does two jobs at once. It makes prompts reusable (the parameterisation keeps
us from storing dozens of near-identical variants), and it's our primary data
control — if the canonical prompt has no real values in it, it can't leak any.
Document each placeholder in the file's Placeholders table with a **safe**
example value.

---

## PII & proprietary-data checklist

Run this before opening a PR. Reviewers run it again before merging.

- [ ] **No personal data.** No real names, emails, phone numbers, addresses,
      employee or customer identifiers — in the prompt, the examples, or the
      metadata.
- [ ] **No proprietary data.** No internal figures, unreleased plans, client
      names, credentials, API keys, or confidential document contents.
- [ ] **Situation-specific values are placeholders.** Anything that would vary
      per use is a `[BRACKETED]` token, not a literal.
- [ ] **Examples are synthetic.** Any sample input/output uses invented, safe
      values only.
- [ ] **Metadata is clean.** `author`/`source` don't expose anything sensitive.

If a prompt genuinely can't be made safe with placeholders, it doesn't belong in
the shared library — keep it in your own private notes instead.

---

## Naming conventions

- **Files:** `kebab-case`, matching the `id`, e.g. `meeting-action-items.md`.
- **IDs:** lowercase, hyphenated, stable for life.
- **Tags:** lowercase, singular where natural (`summary` not `summaries`), reuse
  before you invent.

---

## How versioning works here

Two layers, both intentional:

- **Git history** is authoritative. Every merge is a dated, attributed commit
  with a full diff. Nothing is ever overwritten.
- **The `version` field + Changelog** in each file is the human-readable summary,
  so people who don't read Git can still see what changed and why.

Bump the version and add a changelog line on every meaningful edit. Trivial typo
fixes don't need a bump.
