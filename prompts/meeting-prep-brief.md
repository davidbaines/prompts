---
title: Meeting prep brief
id: meeting-prep-brief
purpose: Assemble the context, open items and one goal for an upcoming meeting, so you walk in prepared without digging through history.
tags: [meetings, briefing, preparation, planning]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 9
automation: scheduled-or-triggered
triggers: [calendar, cron]
---

## Prompt

```text
Prepare me for a meeting.

Give me:
1. The one outcome that would make this meeting a success — inferred from what
   I provide; if my goal isn't clear from it, ask me before writing.
2. Where things left off last time, and any open action items owed by either
   side.
3. Up to 3 questions I should ask or points I should raise.
4. Anything I should send or read before it starts.

One page maximum. Skip a section if there's nothing real to say.

The meeting details (what, who, when, what I want out of it) and any prior
notes or threads follow:

[PASTE THE MEETING DETAILS AND PRIOR CONTEXT HERE]
```

## Placeholders

| Placeholder                                       | Meaning                                          | Safe example        |
|---------------------------------------------------|--------------------------------------------------|---------------------|
| `[PASTE THE MEETING DETAILS AND PRIOR CONTEXT HERE]` | A line on the meeting plus prior notes — the only thing to supply | *(private content)* |

## Usage & automation notes

- **Adjusting it:** put it in the same message — "the goal is to agree a
  renewal timeline", "keep it to five lines".
- **Scheduled/triggered:** run each morning against the day's calendar so a brief
  is ready for every meeting with prior context attached.
- Feed it the last meeting's summary (from `meeting-summary-actions`) as the
  prior context to close the loop between meetings.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: single paste slot last,
  goal inferred or asked for rather than a required field. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
