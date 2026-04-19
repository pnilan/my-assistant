---
status: open
started: 2026-04-19
---

# 0012 — Timeout strategy

## Context

Siri abandons the intent after ~10–30s. Some agent loops (many tool calls,
large lists) may exceed that.

## Options

- **Synchronous with hard cap** — server enforces e.g. 8s; returns a graceful
  "this is taking too long" reply on exceed. MVP default.
- **Ack + push notification** — reply immediately with "working on it" and
  deliver the real answer as a push notification later. More complex; better
  UX for long operations.

## Decision

TBD — MVP likely synchronous; push-notification fallback as Phase 6 stretch.

## Consequences

TBD.
