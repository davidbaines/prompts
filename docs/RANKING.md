# Ranked starter set: high-leverage office prompts

Twelve prompts chosen and ranked against three criteria:

- **T — Time/effort saved:** magnitude of the saving multiplied by how often the
  task recurs. A big one-off saving scores lower than a moderate daily one.
- **B — Breadth:** how many office roles can use it more or less as-is.
- **A — Automatability:** can it run unattended on a schedule (cron) or fire from
  a trigger (a new email, a Slack message, a calendar event)? Purely interactive
  prompts score low here even when they're excellent.

Each is scored 1–5 per criterion. Where totals tie, the more automatable prompt
ranks higher, since that was the hardest of the three criteria to satisfy.

## Schema note

These files extend the base schema (see `README.md`) with two fields that matter
for this set:

- `automation:` — `interactive`, `scheduled`, `triggered`, or `scheduled-or-triggered`.
- `triggers:` — list of firing mechanisms, e.g. `[cron, email, slack, calendar]`.

This is the schema doing its job: when a new dimension matters, add a field rather
than bolting it onto tags.

## The ranking

| # | Prompt | id | T | B | A | Total | How it runs |
|---|--------|----|---|---|---|-------|-------------|
| 1 | Email thread summary + suggested reply | `email-thread-summary-reply` | 5 | 5 | 5 | 15 | Fires on a new/flagged email; also interactive |
| 2 | Weekly status digest from many sources | `weekly-status-digest` | 5 | 4 | 5 | 14 | Cron, e.g. Friday 08:00 across set channels |
| 3 | Daily morning brief | `daily-morning-brief` | 4 | 5 | 5 | 14 | Cron each workday morning |
| 4 | Meeting notes to summary + action items | `meeting-summary-actions` | 5 | 5 | 4 | 14 | Fires when a transcript is ready; also interactive |
| 5 | Inbox triage and prioritisation | `inbox-triage` | 4 | 5 | 5 | 14 | Cron or on new mail |
| 6 | Support/request ticket triage + draft reply | `ticket-triage-draft` | 4 | 4 | 5 | 13 | Fires on a new ticket, email, or Slack message |
| 7 | Action-item extractor (any thread or doc) | `action-item-extractor` | 4 | 5 | 4 | 13 | Runs on a thread/doc on a schedule or trigger |
| 8 | Long document / report summariser | `document-summariser` | 5 | 5 | 3 | 13 | Mostly interactive; can fire when a file arrives |
| 9 | Meeting prep brief | `meeting-prep-brief` | 4 | 4 | 4 | 12 | Fires the morning of, from the calendar |
| 10 | Competitive / market brief on a company | `competitive-brief` | 4 | 3 | 4 | 11 | Cron (weekly/monthly) or interactive |
| 11 | Rough notes to polished message | `notes-to-message` | 4 | 5 | 2 | 11 | Interactive |
| 12 | Proofread and clarity pass | `proofread-clarity-pass` | 3 | 5 | 2 | 10 | Interactive |

## Reading the ranking

The top of the table is where all three criteria line up: universal tasks that
eat real time and can be left to run on their own. Nine of the twelve can be
scheduled or triggered; the three interactive ones (`notes-to-message`,
`proofread-clarity-pass`, and to a degree `document-summariser`) earn their place
on breadth and per-use time saving, since almost everyone does them many times a
day.

## A data-handling note for the automated ones

The prompts themselves hold no real data — they use placeholders, so they stay
safe to share (see the PII checklist in `README.md`). But when you *automate* one,
real email or message content flows through whatever platform runs it (ChatGPT
Tasks, Claude Cowork, Slack Workflow Builder, Zapier, and so on). Keeping PII out
of the shared prompt is handled; deciding which content an automation is allowed
to read is a separate call to make per workflow.
