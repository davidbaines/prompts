---
title: Email thread summary + suggested reply
id: email-thread-summary-reply
purpose: Condense a long email thread into what matters and draft a reply, so you act on a message in seconds instead of re-reading it.
tags: [email, summarizing, drafting, inbox]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 1
automation: scheduled-or-triggered
triggers: [email, cron]
---

## Prompt

```text
You are a sharp executive assistant.

Summarise the email thread below in 3–4 lines: who wants what, and where it
stands now. List any explicit questions or requests directed at me — I'm the
recipient of the most recent message unless I say otherwise. Then draft a
reply in a warm, concise tone, under 120 words, that addresses each of those.
Use [SQUARE_BRACKET] markers for anything you can't infer (dates, figures,
names). If the thread needs no reply from me, say so instead of drafting one.

Adjust tone or length if I ask. The thread follows:

[PASTE THE EMAIL THREAD HERE]
```

## Placeholders

| Placeholder                     | Meaning                              | Safe example        |
|---------------------------------|--------------------------------------|---------------------|
| `[PASTE THE EMAIL THREAD HERE]` | The thread — the only thing to supply | *(private content)* |

The `[SQUARE_BRACKET]` line is an instruction to the model, not something to
fill in.

## Usage & automation notes

- **Adjusting it:** say it in the same message rather than editing the prompt —
  "formal", "under 60 words", "I'm Sam in this thread".
- The "no reply needed" escape hatch stops it inventing busywork.
- **Connected:** with a mail connector (Claude or ChatGPT Gmail connector,
  Gemini in Gmail) skip the paste entirely — ask it to summarise the thread
  directly. **Triggered:** an automation tool (Zapier, Make) can run it on a
  starred/labelled incoming email so a draft is waiting when you open the
  message.
- Review every draft before sending; treat it as a first draft, never a final one.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  paste slot last. Automation note updated to connector routes. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
