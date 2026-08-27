---
title: Rough notes to polished message
id: notes-to-message
purpose: Turn bullet points or a half-formed thought into a clear, well-pitched message, so writing a note takes seconds not minutes.
tags: [drafting, writing, email, communication]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 11
automation: interactive
triggers: []
---

## Prompt

```text
Turn my rough notes into a finished message.

Default to an email in a professional, warm tone, under 120 words — adjust if
I name a different channel, audience, tone, length, or goal. Infer the
audience and goal from the notes where you can.

Keep my meaning and any specific facts exactly; don't add claims I didn't
make. Lead with the point. If the notes are missing something the message
needs, ask me one question rather than inventing it.

My notes follow:

[PASTE YOUR ROUGH NOTES HERE]
```

## Placeholders

| Placeholder                   | Meaning                                  | Safe example        |
|-------------------------------|------------------------------------------|---------------------|
| `[PASTE YOUR ROUGH NOTES HERE]` | Your rough input — the only thing to supply | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "Slack message", "for a client
  I've not met", "goal: book a call next week".
- Interactive by nature — it starts from your intent each time, so it isn't a
  schedule/trigger candidate.
- The "don't add claims I didn't make" rule guards against the model embellishing.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  paste slot last. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
