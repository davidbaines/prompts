---
title: Rough notes to polished message
id: notes-to-message
purpose: Turn bullet points or a half-formed thought into a clear, well-pitched message, so writing a note takes seconds not minutes.
tags: [drafting, writing, email, communication]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 11
automation: interactive
triggers: []
---

## Prompt

```text
Turn my rough notes into a finished [CHANNEL] message.

Notes:
[NOTES]

- Audience: [AUDIENCE]
- Tone: [TONE]
- Length: [LENGTH]
- Goal: [GOAL]

Keep my meaning and any specific facts exactly; don't add claims I didn't make.
Lead with the point. If the notes are missing something the message needs, ask me
one question rather than inventing it.
```

## Placeholders

| Placeholder  | Meaning                    | Safe example              |
|--------------|----------------------------|---------------------------|
| `[CHANNEL]`  | Where it's going           | email / Slack / LinkedIn  |
| `[NOTES]`    | Your rough input           | *(supplied at use)*       |
| `[AUDIENCE]` | Who receives it            | a client I've not met     |
| `[TONE]`     | Register                   | professional, warm        |
| `[LENGTH]`   | Target length              | under 120 words           |
| `[GOAL]`     | What it should achieve     | book a call next week     |

## Usage & automation notes

- Interactive by nature — it starts from your intent each time, so it isn't a
  schedule/trigger candidate.
- The "don't add claims I didn't make" rule guards against the model embellishing.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
