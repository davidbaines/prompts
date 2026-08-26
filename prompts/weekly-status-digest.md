---
title: Weekly status digest from many sources
id: weekly-status-digest
purpose: Pull a week of scattered updates into one crisp status summary, replacing the manual Friday round-up.
tags: [reporting, summarizing, internal-comms, status]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 2
automation: scheduled
triggers: [cron, slack]
---

## Prompt

```text
You are a chief of staff writing a weekly status for [AUDIENCE].

Here are this week's raw updates from [SOURCES]:
[RAW_UPDATES]

Produce a summary that reads in under a minute:
- Open with the single most important development of the week.
- Then three sections: Progress, Blockers, Next.
- One line per item. Cut filler. Merge duplicates.
- Flag anything that stalled or slipped, and anything awaiting a decision.
- If a section has nothing real to report, write "Nothing to flag."

Output format: [OUTPUT_FORMAT]
```

## Placeholders

| Placeholder       | Meaning                        | Safe example                     |
|-------------------|--------------------------------|----------------------------------|
| `[AUDIENCE]`      | Who reads it                   | the leadership team              |
| `[SOURCES]`       | Where updates came from        | five project channels            |
| `[RAW_UPDATES]`   | The week's messages/notes      | *(pulled at run time)*           |
| `[OUTPUT_FORMAT]` | Shape of output                | markdown with three sub-headings |

## Usage & automation notes

- This is the canonical schedulable prompt. Slack Workflow Builder's AI step can
  run it every Friday against named channels and post to `#exec-updates`; ChatGPT
  Tasks and Claude Cowork do the same on a cron.
- "Nothing to flag" prevents the model padding thin weeks with invented progress.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
