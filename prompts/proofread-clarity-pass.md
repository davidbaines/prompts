---
title: Proofread and clarity pass
id: proofread-clarity-pass
purpose: A light editing pass that fixes errors and improves clarity while keeping your voice, so anything you send reads cleanly.
tags: [editing, proofreading, writing, clarity]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 12
automation: interactive
triggers: []
---

## Prompt

```text
Do a light editing pass on the text below.
[TEXT]

- Fix spelling, grammar and punctuation.
- Improve clarity and flow only where it genuinely helps.
- Keep my voice and word choices; don't rewrite for the sake of it.
- Don't change meaning, add content, or inflate the length.
- Use [BRITISH_OR_US] English.

Return two things: the edited text, then a short list of the substantive changes
(ignore trivial typo fixes) so I can see what you altered.
```

## Placeholders

| Placeholder        | Meaning              | Safe example |
|--------------------|----------------------|--------------|
| `[TEXT]`           | What to edit         | *(at use)*   |
| `[BRITISH_OR_US]`  | Spelling convention  | British      |

## Usage & automation notes

- Asking for the change list keeps it honest and lets you reject over-editing.
- Interactive: it edits what you're writing now, so there's nothing to schedule.
- The "keep my voice / don't rewrite for the sake of it" instruction is what stops
  it flattening everything into generic prose.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
