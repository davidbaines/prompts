---
# Metadata schema. Fill every required field. Put the value before the # comment.
# Required fields:
title:        # Short human-readable name, e.g. "Weekly status summary"
id:           # Lowercase kebab-case slug. Must equal the filename. Never change once set.
purpose:      # One sentence: what this prompt does and when to reach for it.
tags: []      # Discovery keywords, e.g. [summarizing, email, internal-comms]. Reuse existing tags.
models: []    # Models it was tuned on, e.g. [claude, gpt, gemini] or a specific version.
author:       # Who wrote or first contributed this.
source:       # "original" if yours, otherwise where it was adapted from (name or URL).
version: 1    # Integer, bumped on every meaningful change (see Changelog below).
created:      # YYYY-MM-DD
updated:      # YYYY-MM-DD
status: draft # draft | reviewed | proven | deprecated. New prompts start as draft.
# Optional fields. Keep them if the prompt can run unattended; otherwise leave the
# defaults below (interactive, no triggers).
automation: interactive  # interactive | scheduled | triggered | scheduled-or-triggered
triggers: []             # Any of [cron, email, slack, calendar]. Empty for interactive.
---

## Prompt

<!--
Write the prompt in the ZERO-EDIT style: the user should copy it, paste their
content, and send — with nothing to hand-edit.

- Bake choices in as defaults with a spoken override, e.g. "in a warm, concise
  tone, under 120 words — adjust if I ask", instead of [TONE] and [WORD_LIMIT]
  fields. A prompt that needs five fields edited is slower than doing the task
  by hand.
- Exactly ONE required slot, placed LAST, named for the action:
  [PASTE THE ... HERE]. Content last means: copy prompt, paste content, send.
- Where the model may need to mark unknowns in its OUTPUT, instruct it to use
  [SQUARE_BRACKET] markers — and note under Placeholders that this line is an
  instruction, not a fill-in.
- NEVER paste real PII or proprietary data anywhere in this file. The canonical
  prompt must be safe to share; real values are supplied privately at use time.
-->

```text
You are [a role, written in plain words, not a placeholder].

[The task, with every choice stated as a default the user can override by
saying so — tone, length, audience, format.]

[What to do when information is missing: ask one question, or mark unknowns
with [SQUARE_BRACKET] placeholders — never invent.]

The [content] follows:

[PASTE THE CONTENT HERE]
```

## Placeholders

<!-- Usually a single row: the one paste slot. Keep example values SAFE. -->

| Placeholder                | Meaning                                    | Safe example        |
|----------------------------|--------------------------------------------|---------------------|
| `[PASTE THE CONTENT HERE]` | The input — the only thing to supply       | *(private content)* |

## Usage & automation notes

<!--
Start with an "Adjusting it" bullet: the overrides a user can speak instead of
editing ("formal", "under 60 words", "for the sales team"). Then tips, gotchas,
and what good or bad output looks like. If the prompt suits a connector (mail,
calendar) or a schedule/trigger, say how it runs and what replaces the paste.
-->

- **Adjusting it:** say it in the same message — "…", "…".
-

## Example (optional)

<!-- A short sample run using SAFE placeholder values only. -->

**Filled prompt:**

```text

```

**Sample output:**

```text

```

## Changelog

<!--
The Git commit history is the authoritative version log. This section is the
human-readable summary. Add a line each time you bump the version field.
-->

- **v1** (YYYY-MM-DD): Initial version. [author]
