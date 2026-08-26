## What this PR does

<!-- One or two lines. New prompt, edit to an existing prompt, or tooling/docs. -->

## PII & proprietary-data checklist

Tick every box. A reviewer checks these again before merge.

- [ ] **No personal data.** No real names, emails, phone numbers, addresses, or employee/customer identifiers in the prompt, examples, or metadata.
- [ ] **No proprietary data.** No internal figures, unreleased plans, client names, credentials, API keys, or confidential document contents.
- [ ] **Situation-specific values are placeholders.** Anything that varies per use is a `[BRACKETED]` token, not a literal.
- [ ] **Examples are synthetic.** Any sample input or output uses invented, safe values only.
- [ ] **Metadata is clean.** `author` and `source` expose nothing sensitive.

## For a new or changed prompt

- [ ] Copied from `templates/TEMPLATE.md`; all required frontmatter fields are filled.
- [ ] `id` is lowercase kebab-case and matches the filename.
- [ ] `python scripts/validate.py` passes with no errors.
- [ ] For an edit: `version` bumped and a changelog line added.
- [ ] `python scripts/update_index.py` run, and the regenerated `INDEX.md` is included in this PR.

<!-- Delete the "new or changed prompt" section if this PR only touches tooling or docs. -->
