---
title: Support/request ticket triage + draft reply
id: ticket-triage-draft
purpose: Classify an incoming ticket or request and draft a first response, so agents open a case already halfway answered.
tags: [support, triage, drafting, ops, it-helpdesk]
models: [claude, gpt, gemini]
author: Curated set
source: original
version: 1
created: 2026-08-25
updated: 2026-08-25
status: reviewed
rank: 6
automation: triggered
triggers: [email, slack]
---

## Prompt

```text
You handle incoming [QUEUE_NAME] requests.

New request:
[TICKET]

Reference material you may rely on (do not invent beyond it):
[KNOWLEDGE_SOURCE]

Return:
1. Category: [CATEGORIES] — pick one.
2. Urgency: low / medium / high, with a one-line reason.
3. Draft reply in a [TONE] tone that either resolves it or asks the one question
   needed to proceed. Mark anything you're unsure of with [PLACEHOLDER].
4. Escalate? Yes/No — say Yes if it needs a human decision or falls outside the
   reference material, and state why.
```

## Placeholders

| Placeholder          | Meaning                        | Safe example                     |
|----------------------|--------------------------------|----------------------------------|
| `[QUEUE_NAME]`       | Which queue                    | IT helpdesk                      |
| `[TICKET]`           | The incoming request           | *(supplied at run)*              |
| `[KNOWLEDGE_SOURCE]` | Approved reference content     | *(FAQ / policy doc)*             |
| `[CATEGORIES]`       | Allowed categories             | access, hardware, billing, other |
| `[TONE]`             | Reply register                 | friendly and clear               |

## Usage & automation notes

- The "escalate" flag and "don't invent beyond the reference" clause keep it from
  confidently answering things it shouldn't.
- **Triggered:** fire on a new ticket/email/Slack message; post the draft as an
  internal note for an agent to approve, not an auto-send to the requester.

## Changelog

- **v1** (2026-08-25) — Initial version. Curated set
