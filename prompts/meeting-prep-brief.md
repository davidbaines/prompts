---
title: Meeting prep brief
id: meeting-prep-brief
purpose: Assemble the context, open items and one goal for an upcoming meeting, so you walk in prepared without digging through history.
tags: [meetings, briefing, preparation, planning]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 9
automation: scheduled-or-triggered
triggers: [calendar, cron]
---

## Prompt

```text
Prepare me for a meeting.

- Meeting: [MEETING_TITLE] with [ATTENDEES] at [TIME].
- Prior context (last notes, relevant thread, or doc): [CONTEXT]
- What I want out of it: [GOAL]

Give me:
1. The one outcome that would make this meeting a success.
2. Where things left off last time, and any open action items owed by either side.
3. Up to 3 questions I should ask or points I should raise.
4. Anything I should send or read before it starts.

One page maximum. Skip a section if there's nothing real to say.
```

## Placeholders

| Placeholder       | Meaning                | Safe example              |
|-------------------|------------------------|---------------------------|
| `[MEETING_TITLE]` | Which meeting          | the vendor check-in       |
| `[ATTENDEES]`     | Who's attending        | the account manager       |
| `[TIME]`          | When                   | 2pm today                 |
| `[CONTEXT]`       | Relevant prior material| *(supplied at run)*       |
| `[GOAL]`          | Your aim               | agree a renewal timeline  |

## Usage & automation notes

- **Scheduled/triggered:** run each morning against the day's calendar so a brief
  is ready for every meeting with prior context attached.
- Feed it the last meeting's summary (from `meeting-summary-actions`) as `[CONTEXT]`
  to close the loop between meetings.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
