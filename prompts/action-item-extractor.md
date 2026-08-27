---
title: Action-item extractor (any thread or doc)
id: action-item-extractor
purpose: Pull every commitment, owner and due date out of any block of text, so nothing agreed in passing gets lost.
tags: [action-items, extraction, follow-up, accountability]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 7
automation: scheduled-or-triggered
triggers: [slack, cron, email]
---

## Prompt

```text
Read the text below and extract only the commitments — things someone said
they would do.

Return a table: Owner | Action | Due | Source quote.
- One row per distinct commitment.
- "Source quote" is the short phrase the commitment came from, so it can be
  verified.
- If owner or due date is missing, write "unassigned" / "no date". Never guess.
- If there are no real commitments, say so plainly. Do not manufacture tasks.

The text follows:

[PASTE THE THREAD, TRANSCRIPT, OR DOCUMENT HERE]
```

## Placeholders

| Placeholder                                    | Meaning                                | Safe example        |
|------------------------------------------------|----------------------------------------|---------------------|
| `[PASTE THE THREAD, TRANSCRIPT, OR DOCUMENT HERE]` | The text to mine — the only thing to supply | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "only my commitments", "as a
  checklist rather than a table".
- Differs from `meeting-summary-actions`: no summary, works on any text, and quotes
  its source so each item is checkable.
- **Triggered/scheduled:** run over a busy channel end-of-day to catch commitments
  that never made it onto a task list.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: single paste slot moved
  last. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
