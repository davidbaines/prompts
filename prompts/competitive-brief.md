---
title: Competitive / market brief on a company
id: competitive-brief
purpose: Produce a structured brief on a named competitor or market, so recurring research becomes a scheduled report instead of a manual scramble.
tags: [research, competitive, market, briefing, sales]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 10
automation: scheduled
triggers: [cron]
---

## Prompt

```text
You are a market analyst. Produce a brief on [COMPANY] for [AUDIENCE].

Cover, in this order:
1. What they do, in two lines.
2. Recent moves: launches, announcements, or changes in the last [PERIOD].
3. Positioning: who they target and how they differ from [OUR_ANGLE].
4. Signals: notable customer sentiment, hiring, or pricing changes if evident.
5. So what: 2–3 implications for us, stated as actions we could consider.

Use only information you can support. Where you're unsure or lack current data,
say so rather than speculating. Note the date of anything time-sensitive.
```

## Placeholders

| Placeholder    | Meaning                       | Safe example              |
|----------------|-------------------------------|---------------------------|
| `[COMPANY]`    | Subject of the brief          | a named competitor        |
| `[AUDIENCE]`   | Who reads it                  | the sales team            |
| `[PERIOD]`     | Look-back window              | the last quarter          |
| `[OUR_ANGLE]`  | Your own positioning          | our mid-market focus      |

## Usage & automation notes

- Pair with a model that has current web access, or supply source material, since
  this depends on recent facts.
- **Scheduled:** run monthly per key competitor and post to a research channel.
  The "say so rather than speculate" clause is essential when it runs unattended.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
