---
status: open
started: 2026-04-19
---

# 0014 — Testing framework

## Context

Unit tests are expected from Phase 1. Need a framework and a split between
unit / integration / eval.

## Options

- **pytest + pytest-asyncio + httpx.AsyncClient** — de facto Python standard.
- **unittest** (stdlib) — no dependency; more verbose.

Additional: how to mark the eval suite so it runs separately from unit tests
(`pytest -m eval`, or a separate directory).

## Decision

TBD.

## Consequences

TBD.
