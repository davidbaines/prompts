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
Write the prompt below. Use [SQUARE_BRACKET] placeholders for anything that would
otherwise be a real name, number, client, internal figure, or document. NEVER
paste real PII or proprietary data here. The canonical prompt must be safe to
share. Real values are filled in privately at use time.
-->

```text
You are [ROLE].

Context: [CONTEXT]

Task: [TASK]

Constraints:
- [CONSTRAINT_1]
- [CONSTRAINT_2]

Output format: [OUTPUT_FORMAT]
```

## Placeholders

<!-- Explain each placeholder and give a SAFE, non-sensitive example value. -->

| Placeholder       | Meaning                        | Safe example              |
|-------------------|--------------------------------|---------------------------|
| `[ROLE]`          | Persona the model should adopt | a concise project manager |
| `[CONTEXT]`       | Background the model needs     | notes from a team standup |
| `[TASK]`          | The actual instruction         | summarise into 5 bullets  |
| `[OUTPUT_FORMAT]` | Shape of the desired output    | markdown bullet list      |

## Usage & automation notes

<!--
Tips, gotchas, and what good or bad output looks like. If the prompt is
schedulable or trigger-driven, say how it fires and on what (a new email, a Slack
message, a cron time). Note any guard clause that matters when it runs unattended.
-->

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
