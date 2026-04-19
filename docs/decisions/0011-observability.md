---
status: open
started: 2026-04-19
---

# 0011 — Observability

## Context

Agents misbehave in ways that are hard to debug from outside. Need visibility
into tool calls, prompts, latencies.

## Options

- **stdout logs** — baseline; grep-able.
- **structured logs** (structlog / loguru + JSON) — queryable, ships to
  Datadog/Loki later.
- **Pydantic Logfire** — native integration with Pydantic AI, shows agent
  traces, tool calls, token counts.
- **OpenTelemetry** — vendor-neutral, more setup.

## Decision

TBD.

## Consequences

TBD.
