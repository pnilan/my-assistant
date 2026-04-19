---
status: open
started: 2026-04-19
---

# 0008 — State / conversation memory

## Context

Should the server remember prior turns so follow-ups ("what about next week?")
work, or is each request independent?

## Options

- **Stateless** — each POST is fresh. Simple, cheap. No follow-ups.
- **Short conversation history** — keep last N turns keyed by device/user.
  Enables follow-ups; requires session concept and storage.

## Decision

TBD. Default to stateless for MVP; revisit in Phase 6 if follow-ups become
important.

## Consequences

TBD.
