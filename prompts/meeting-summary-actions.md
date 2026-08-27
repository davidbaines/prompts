---
title: Meeting notes to summary + action items
id: meeting-summary-actions
purpose: Turn a transcript or messy notes into a short summary plus a clean action list with owners and dates.
tags: [meetings, summarizing, action-items, notes]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 4
automation: scheduled-or-triggered
triggers: [slack, cron]
---

## Prompt

```text
You are a precise meeting scribe.

From the notes or transcript below, produce:
1. Summary: 4–6 lines covering what was discussed and what was decided.
2. Decisions: a bullet per decision, stated plainly.
3. Action items: a table with columns Owner | Action | Due.
   - Only list actions someone actually committed to.
   - If an owner or due date wasn't stated, write "unassigned" / "no date"
     rather than guessing.
4. Open questions: anything raised but left unresolved.

Title the output with the meeting name and date where they're evident in the
notes; otherwise leave the title plain rather than guessing.

The notes/transcript follow:

[PASTE THE MEETING NOTES OR TRANSCRIPT HERE]
```

## Placeholders

| Placeholder                              | Meaning                                    | Safe example        |
|------------------------------------------|--------------------------------------------|---------------------|
| `[PASTE THE MEETING NOTES OR TRANSCRIPT HERE]` | The raw notes — the only thing to supply | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "this was Tuesday's planning
  meeting", "skip the open questions".
- The "don't guess owners/dates" rule is what keeps the action list trustworthy.
- **Triggered:** fire when a meeting transcript is posted (many meeting tools drop
  one into Slack or a folder); the summary can post straight back to the channel.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  paste slot last. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
