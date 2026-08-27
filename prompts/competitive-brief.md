---
title: Competitive / market brief on a company
id: competitive-brief
purpose: Produce a structured brief on a named competitor or market, so recurring research becomes a scheduled report instead of a manual scramble.
tags: [research, competitive, market, briefing, sales]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 10
automation: scheduled
triggers: [cron]
---

## Prompt

```text
You are a market analyst. Produce a brief on the company or market named
below, for an internal team audience — adjust if I name a different audience.

Cover, in this order:
1. What they do, in two lines.
2. Recent moves: launches, announcements, or changes in the last quarter, or
   another window if I give one.
3. Positioning: who they target and how they differ from us. Use whatever I've
   told you about our own positioning; if I've said nothing about it, ask one
   question before writing.
4. Signals: notable customer sentiment, hiring, or pricing changes if evident.
5. So what: 2–3 implications for us, stated as actions we could consider.

Use only information you can support. Where you're unsure or lack current
data, say so rather than speculating. Note the date of anything time-sensitive.

The subject follows:

[TYPE THE COMPANY OR MARKET NAME HERE]
```

## Placeholders

| Placeholder                            | Meaning                                   | Safe example       |
|----------------------------------------|-------------------------------------------|--------------------|
| `[TYPE THE COMPANY OR MARKET NAME HERE]` | The subject — the only thing to supply    | a named competitor |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "for the sales team", "last
  six months", "our angle is mid-market pricing".
- Pair with a model that has current web access, or supply source material, since
  this depends on recent facts.
- **Scheduled:** run monthly per key competitor and post to a research channel.
  The "say so rather than speculate" clause is essential when it runs unattended.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  subject slot last, positioning asked for when unknown. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
