---
title: Daily morning brief
id: daily-morning-brief
purpose: Assemble calendar, inbox and priorities into a one-screen brief so the day starts without the usual tab-opening ritual.
tags: [briefing, planning, email, calendar, summarizing]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 3
automation: scheduled
triggers: [cron]
---

## Prompt

```text
You are my early-morning chief of staff. It is [DATE].

Inputs:
- Today's meetings: [CALENDAR]
- Overnight/unread messages worth noting: [MESSAGES]
- My stated priorities this week: [PRIORITIES]

Give me a brief I can read in 60 seconds:
1. The 3 things that most need my attention today, and why.
2. Meetings I should prepare for, with the one thing to do before each.
3. Anything time-sensitive that will slip if I don't act today.

Keep it tight. If nothing is urgent, say the day is clear and why.
```

## Placeholders

| Placeholder     | Meaning                       | Safe example              |
|-----------------|-------------------------------|---------------------------|
| `[DATE]`        | Today's date                  | Tuesday 25 August         |
| `[CALENDAR]`    | Today's events                | *(pulled at run time)*    |
| `[MESSAGES]`    | Overnight items of note       | *(pulled at run time)*    |
| `[PRIORITIES]`  | Your current focus            | ship the onboarding flow  |

## Usage & automation notes

- Best run on a cron each workday before you start (ChatGPT Tasks, Claude Cowork).
  Connect a calendar/mail source so `[CALENDAR]` and `[MESSAGES]` fill themselves.
- Start with just the calendar for two weeks, then add sources once you trust it.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
