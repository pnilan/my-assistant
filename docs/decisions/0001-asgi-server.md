---
status: open
started: 2026-04-19
---

# 0001 — ASGI server

## Context

FastAPI needs an ASGI server to actually serve HTTP. The choice affects
latency, HTTP version support, and ops ergonomics, but is swappable later.

## Options

- **uvicorn** — most common default, `uvloop` + `httptools`, great docs.
- **hypercorn** — HTTP/2 and HTTP/3 support, Trio compatibility.
- **granian** — Rust-based, measurably faster under load.

## Decision

TBD.

## Consequences

TBD.

## Related

- Phase 1 in [`plans/00-overview.md`](../plans/00-overview.md).
