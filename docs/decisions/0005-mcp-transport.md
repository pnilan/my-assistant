---
status: open
started: 2026-04-19
---

# 0005 — MCP transport

## Context

Pydantic AI can connect to remote MCP servers over Streamable HTTP or SSE.
We need to know which Agent Engine actually serves.

## Options

- **Streamable HTTP** (`MCPServerStreamableHTTP`) — current MCP default.
- **SSE** (`MCPServerHTTP`) — older transport, still common.

## Decision

TBD — confirm from Agent Engine documentation or admin UI before Phase 1.

## Consequences

TBD.

## Related

- Blocks Phase 1 in [`plans/00-overview.md`](../plans/00-overview.md).
