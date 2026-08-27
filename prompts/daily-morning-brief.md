---
title: Daily morning brief
id: daily-morning-brief
purpose: Assemble calendar, inbox and priorities into a one-screen brief so the day starts without the usual tab-opening ritual.
tags: [briefing, planning, email, calendar, summarizing]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 3
automation: scheduled
triggers: [cron]
---

## Prompt

```text
You are my early-morning chief of staff.

From the material below (or, if you have calendar and mail access, by fetching
today's events and unread messages yourself), give me a brief I can read in
60 seconds:
1. The 3 things that most need my attention today, and why.
2. Meetings I should prepare for, with the one thing to do before each.
3. Anything time-sensitive that will slip if I don't act today.

Keep it tight. If nothing is urgent, say the day is clear and why.

Today's calendar, notable unread messages, and my current priorities follow:

[PASTE TODAY'S CALENDAR, NOTABLE MESSAGES, AND PRIORITIES HERE]
```

## Placeholders

| Placeholder | Meaning | Safe example |
|-------------|---------|--------------|
| `[PASTE TODAY'S CALENDAR, NOTABLE MESSAGES, AND PRIORITIES HERE]` | The day's inputs — the only thing to supply, and unnecessary with connectors | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "top 5 not 3", "ignore the
  inbox today".
- **Connected:** with calendar and mail connectors there is nothing to paste at
  all — the brief becomes a one-line request. Best run on a schedule each
  workday before you start.
- Start with just the calendar for two weeks, then add sources once you trust it.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  paste slot last, connector route noted. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
