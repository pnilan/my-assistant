---
status: open
started: 2026-04-19
---

# 0006 — Model choice

## Context

Voice flow is latency-sensitive (~8s budget end-to-end). Model needs to handle
tool-selection across MCP tools and produce short spoken replies.

## Options

- **Claude Haiku 4.5** — fast, cheap, usually adequate for tool-calling.
- **Claude Sonnet 4.6** — smarter, slower, better with ambiguous queries.
- **Claude Opus 4.7** — best reasoning, too slow for voice in most cases.

## Decision

TBD. Start with one, revisit based on Phase 2 eval pass rate.

## Consequences

TBD.

## Related

- Phase 2 evaluation in [`plans/00-overview.md`](../plans/00-overview.md).
