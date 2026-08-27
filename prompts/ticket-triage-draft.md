---
title: Support/request ticket triage + draft reply
id: ticket-triage-draft
purpose: Classify an incoming ticket or request and draft a first response, so agents open a case already halfway answered.
tags: [support, triage, drafting, ops, it-helpdesk]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 2
created: 2026-08-25
updated: 2026-08-27
status: reviewed
rank: 6
automation: triggered
triggers: [email, slack]
---

## Prompt

```text
You handle incoming support and helpdesk requests — adjust if I name a
specific queue or give my own category list.

For the request below, return:
1. Category: pick the closest of access / hardware / software / billing / other.
2. Urgency: low / medium / high, with a one-line reason.
3. Draft reply in a friendly, clear tone that either resolves it or asks the
   one question needed to proceed. Mark anything you're unsure of with a
   [SQUARE_BRACKET] placeholder. Rely only on reference material included
   below; if none is included, keep the reply procedural rather than factual.
4. Escalate? Yes/No — say Yes if it needs a human decision or falls outside
   the reference material, and state why.

The request (and any reference material, labelled as such) follows:

[PASTE THE TICKET HERE]
```

## Placeholders

| Placeholder              | Meaning                                                    | Safe example        |
|--------------------------|------------------------------------------------------------|---------------------|
| `[PASTE THE TICKET HERE]` | The request, plus any FAQ/policy text you want it to rely on | *(private content)* |

The `[SQUARE_BRACKET]` line is an instruction to the model, not something to
fill in.

## Usage & automation notes

- **Adjusting it:** say it in the same message — "this is the IT helpdesk
  queue", "categories are onboarding, access, other", "formal tone".
- The "escalate" flag and "rely only on included reference material" clause keep
  it from confidently answering things it shouldn't.
- **Triggered:** fire on a new ticket/email/Slack message; post the draft as an
  internal note for an agent to approve, not an auto-send to the requester.

## Changelog

- **v2** (2026-08-27) — Restructured to zero-edit style: defaults inline, single
  paste slot last. David Baines
- **v1** (2026-08-25) — Initial version. Curated set
