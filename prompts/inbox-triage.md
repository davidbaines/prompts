---
title: Inbox triage and prioritisation
id: inbox-triage
purpose: Sort a batch of unread messages into what needs a reply, what to read, and what to ignore, so triage takes a glance not an hour.
tags: [email, inbox, prioritisation, triage]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-26
status: reviewed
rank: 5
automation: scheduled-or-triggered
triggers: [cron, email]
---

## Prompt

```text
You are triaging my inbox. Here are the unread messages:
[MESSAGES]

Sort every message into exactly one of:
- REPLY NEEDED — I have to respond. Add a one-line note on what it wants.
- READ — useful to know, no response needed.
- FYI / IGNORE — low value; safe to skip or archive.

Then give me a "do first" shortlist: the up-to-[N] items most likely to cause a
problem if left today, hardest-first. Be strict; a long shortlist is a useless one.
```

## Placeholders

| Placeholder  | Meaning                    | Safe example         |
|--------------|----------------------------|----------------------|
| `[MESSAGES]` | The unread batch           | *(pulled at run)*    |
| `[N]`        | Max items on the shortlist | 5                    |

## Usage & automation notes

- Sorting into three buckets plus a strict shortlist beats a flat priority score,
  which tends to mark everything "high".
- **Scheduled:** run at set times (e.g. 8am, 1pm) rather than on every mail, so it
  batches instead of interrupting.
- **Field notes (2026-08-26):** with a mail connector the `[MESSAGES]` paste
  disappears entirely — the model reads the unread inbox itself. Proven routes:
  a Claude Code skill or claude.ai Project using the Gmail connector, or a
  Gemini Gem with Workspace access for a second Gmail account. Install once,
  then triage is a single command. Treat flagged-important mail, direct personal
  requests, and near deadlines as shortlist signals.

## Changelog

- **v2** (2026-08-26) — Field notes from first real installation (connector and
  Gem routes; shortlist signals). David Baines
- **v1** (2026-08-25) — Initial version. Curated set
