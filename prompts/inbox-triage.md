---
title: Inbox triage and prioritisation
id: inbox-triage
purpose: Sort a batch of unread messages into what needs a reply, what to read, and what to ignore, so triage takes a glance not an hour.
tags: [email, inbox, prioritisation, triage]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 3
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 5
automation: scheduled-or-triggered
triggers: [cron, email]
---

## Prompt

```text
You are triaging my inbox.

Sort every unread message below (or, if you have mail access, fetch my unread
inbox yourself) into exactly one of:
- REPLY NEEDED — I have to respond; a signature or form counts. Add a one-line
  note on what it wants and any deadline.
- READ — useful to know, no response needed.
- FYI / IGNORE — low value; safe to skip or archive. List these compactly.

Then give me a "do first" shortlist: the up-to-5 items most likely to cause a
problem if left today, hardest first. Be strict; a long shortlist is a useless
one. Flagged-important mail, direct personal requests, and near deadlines are
shortlist signals; a stale unanswered direct request is a strong one.

The unread messages follow:

[PASTE THE UNREAD MESSAGES HERE]
```

## Placeholders

| Placeholder                       | Meaning                                                              | Safe example        |
|-----------------------------------|----------------------------------------------------------------------|---------------------|
| `[PASTE THE UNREAD MESSAGES HERE]` | The unread batch — the only thing to supply, unnecessary with a connector | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "top 3 only", "just today's
  mail", "ignore newsletters entirely".
- Sorting into three buckets plus a strict shortlist beats a flat priority score,
  which tends to mark everything "high".
- **Scheduled:** run at set times (e.g. 8am, 1pm) rather than on every mail, so it
  batches instead of interrupting.
- **Field notes (2026-08-26):** with a mail connector the paste disappears
  entirely — the model reads the unread inbox itself. Proven routes: a Claude
  Code skill or claude.ai Project using the Gmail connector, or a Gemini Gem
  with Workspace access for a second Gmail account. Install once, then triage
  is a single command. An empty shortlist on a quiet day is the rubric working,
  not failing.

## Changelog

- **v3** (2026-08-27) — Restructured to zero-edit style: shortlist size and
  signals baked in, single paste slot last, connector route in the prompt
  itself. David Baines
- **v2** (2026-08-26) — Field notes from first real installation (connector and
  Gem routes; shortlist signals). David Baines
- **v1** (2026-08-25) — Initial version. Curated set
