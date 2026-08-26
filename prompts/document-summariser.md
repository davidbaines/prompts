---
title: Long document / report summariser
id: document-summariser
purpose: Reduce a long document to the points, decisions and risks a busy reader needs, so an hour of reading becomes two minutes.
tags: [summarizing, reading, reports, analysis]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 8
automation: scheduled-or-triggered
triggers: [email, cron]
---

## Prompt

```text
You are briefing a busy [READER_ROLE] who will not read the full document.

Document:
[DOCUMENT]

Produce:
1. Bottom line: 2–3 sentences on what this is and what it means for the reader.
2. Key points: up to [N] bullets, most important first.
3. Decisions or asks: anything requiring a choice or action, and by whom.
4. Risks / caveats: what's uncertain, contested, or missing.
5. Read-in-full if: one line on when the reader should not rely on this summary
   and should read the original instead.

Stay faithful to the document. Note where it's silent rather than filling gaps.
```

## Placeholders

| Placeholder     | Meaning                   | Safe example          |
|-----------------|---------------------------|-----------------------|
| `[READER_ROLE]` | Who it's for              | finance director      |
| `[DOCUMENT]`    | The source text           | *(supplied at run)*   |
| `[N]`           | Max key points            | 7                     |

## Usage & automation notes

- The "read-in-full if" line manages the main risk of summaries: over-trust. It
  tells the reader when the summary is not enough.
- **Triggered:** fire when a report is filed to a folder or mailbox, posting the
  brief alongside the original.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
