---
title: Proofread and clarity pass
id: proofread-clarity-pass
purpose: A light editing pass that fixes errors and improves clarity while keeping your voice, so anything you send reads cleanly.
tags: [editing, proofreading, writing, clarity]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 12
automation: interactive
triggers: []
---

## Prompt

```text
Do a light editing pass on the text below.

- Fix spelling, grammar and punctuation.
- Improve clarity and flow only where it genuinely helps.
- Keep my voice and word choices; don't rewrite for the sake of it.
- Don't change meaning, add content, or inflate the length.
- Match the spelling convention the text already uses (British or US English);
  if it's mixed, use the majority and note that you did.

Return two things: the edited text, then a short list of the substantive
changes (ignore trivial typo fixes) so I can see what you altered.

The text follows:

[PASTE THE TEXT TO EDIT HERE]
```

## Placeholders

| Placeholder                    | Meaning                              | Safe example        |
|--------------------------------|--------------------------------------|---------------------|
| `[PASTE THE TEXT TO EDIT HERE]` | What to edit — the only thing to supply | *(private content)* |

## Usage & automation notes

- **Adjusting it:** say it in the same message — "British English", "be
  stricter", "it's a formal letter".
- Asking for the change list keeps it honest and lets you reject over-editing.
- Interactive: it edits what you're writing now, so there's nothing to schedule.
- The "keep my voice / don't rewrite for the sake of it" instruction is what stops
  it flattening everything into generic prose.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: spelling convention
  inferred from the text, single paste slot last. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
