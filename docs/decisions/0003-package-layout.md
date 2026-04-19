---
status: open
started: 2026-04-19
---

# 0003 — Package layout

## Context

Python package can live at `server/src/my_assistant/` (src-layout) or
`server/my_assistant/` (flat). Affects import behavior and test isolation.

## Options

- **src-layout** — forces install before import; catches packaging mistakes
  early; industry best practice for libraries.
- **flat layout** — simpler; imports work without install; common for apps.

## Decision

TBD.

## Consequences

TBD.
