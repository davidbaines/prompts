---
title: Meeting notes to summary + action items
id: meeting-summary-actions
purpose: Turn a transcript or messy notes into a short summary plus a clean action list with owners and dates.
tags: [meetings, summarizing, action-items, notes]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 4
automation: scheduled-or-triggered
triggers: [slack, cron]
---

## Prompt

```text
You are a precise meeting scribe.

Here are the notes/transcript from [MEETING_NAME] on [DATE]:
[NOTES]

Produce:
1. Summary: 4–6 lines covering what was discussed and what was decided.
2. Decisions: a bullet per decision, stated plainly.
3. Action items: a table with columns Owner | Action | Due.
   - Only list actions someone actually committed to.
   - If an owner or due date wasn't stated, write "unassigned" / "no date" rather than guessing.
4. Open questions: anything raised but left unresolved.
```

## Placeholders

| Placeholder      | Meaning                    | Safe example           |
|------------------|----------------------------|------------------------|
| `[MEETING_NAME]` | Which meeting              | the weekly planning    |
| `[DATE]`         | When it happened           | 25 August              |
| `[NOTES]`        | Transcript or raw notes    | *(supplied at run)*    |

## Usage & automation notes

- The "don't guess owners/dates" rule is what keeps the action list trustworthy.
- **Triggered:** fire when a meeting transcript is posted (many meeting tools drop
  one into Slack or a folder); the summary can post straight back to the channel.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
