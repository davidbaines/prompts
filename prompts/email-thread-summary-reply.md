---
title: Email thread summary + suggested reply
id: email-thread-summary-reply
purpose: Condense a long email thread into what matters and draft a reply, so you act on a message in seconds instead of re-reading it.
tags: [email, summarizing, drafting, inbox]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 1
automation: scheduled-or-triggered
triggers: [email, cron]
---

## Prompt

```text
You are a sharp executive assistant.

Below is an email thread.
[EMAIL_THREAD]

Do three things:
1. Summarise the thread in 3–4 lines: who wants what, and where it stands now.
2. List any explicit questions or requests directed at me, [MY_NAME].
3. Draft a reply in a [TONE] tone that addresses each of those, under [WORD_LIMIT] words.
   Use [PLACEHOLDER] markers for anything you can't infer (dates, figures, names).

If the thread needs no reply from me, say so instead of drafting one.
```

## Placeholders

| Placeholder      | Meaning                     | Safe example        |
|------------------|-----------------------------|---------------------|
| `[EMAIL_THREAD]` | The thread (pasted at use)  | *(private content)* |
| `[MY_NAME]`      | Who "I" am in the thread    | Sam                 |
| `[TONE]`         | Desired register            | warm but concise    |
| `[WORD_LIMIT]`   | Cap on the draft            | 120                 |

## Usage & automation notes

- The "no reply needed" escape hatch stops it inventing busywork.
- **Triggered:** wire to fire on a starred/labelled incoming email (Grok
  Automations, Zapier, Make) so a draft is waiting when you open the message.
- Review every draft before sending; treat it as a first draft, never a final one.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
