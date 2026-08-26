---
title: Action-item extractor (any thread or doc)
id: action-item-extractor
purpose: Pull every commitment, owner and due date out of any block of text, so nothing agreed in passing gets lost.
tags: [action-items, extraction, follow-up, accountability]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 7
automation: scheduled-or-triggered
triggers: [slack, cron, email]
---

## Prompt

```text
Read the text below and extract only the commitments — things someone said they
would do.
[TEXT]

Return a table: Owner | Action | Due | Source quote.
- One row per distinct commitment.
- "Source quote" is the short phrase the commitment came from, so it can be verified.
- If owner or due date is missing, write "unassigned" / "no date". Never guess.
- If there are no real commitments, say so plainly. Do not manufacture tasks.
```

## Placeholders

| Placeholder | Meaning                        | Safe example        |
|-------------|--------------------------------|---------------------|
| `[TEXT]`    | Thread, transcript, or doc     | *(supplied at run)* |

## Usage & automation notes

- Differs from `meeting-summary-actions`: no summary, works on any text, and quotes
  its source so each item is checkable.
- **Triggered/scheduled:** run over a busy channel end-of-day to catch commitments
  that never made it onto a task list.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
