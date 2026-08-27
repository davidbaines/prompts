---
title: Weekly status digest from many sources
id: weekly-status-digest
purpose: Pull a week of scattered updates into one crisp status summary, replacing the manual Friday round-up.
tags: [reporting, summarizing, internal-comms, status]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 2
automation: scheduled
triggers: [cron, slack]
---

## Prompt

```text
You are a chief of staff writing a weekly status summary for a leadership
audience — adjust if I name a different audience.

Produce a summary that reads in under a minute:
- Open with the single most important development of the week.
- Then three sections: Progress, Blockers, Next.
- One line per item. Cut filler. Merge duplicates across sources.
- Flag anything that stalled or slipped, and anything awaiting a decision.
- If a section has nothing real to report, write "Nothing to flag."
Format as markdown with a heading per section, unless I ask for another shape.

This week's raw updates follow:

[PASTE THE WEEK'S UPDATES HERE]
```

## Placeholders

| Placeholder                     | Meaning                                  | Safe example        |
|---------------------------------|------------------------------------------|---------------------|
| `[PASTE THE WEEK'S UPDATES HERE]` | The raw updates — the only thing to supply | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "for the project team", "as a
  Slack post", "plain text".
- This is the canonical schedulable prompt. Slack Workflow Builder's AI step can
  run it every Friday against named channels and post to a status channel;
  scheduled-task features in the chat tools do the same on a cron.
- "Nothing to flag" prevents the model padding thin weeks with invented progress.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  paste slot last. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
