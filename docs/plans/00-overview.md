---
status: draft
phase: 0
started: 2026-04-19
---

# My Assistant — Overview

## Problem

Patrick wants to talk to a personal assistant via Siri (HomePod or iPhone) that
can answer questions about and take actions in his business systems — starting
with Asana (tasks, projects, sections) and expanding to other services over time.

## Success criteria (v1)

- "Hey Siri, ask my assistant what's in the Design section of the Launch project"
  → HomePod speaks back a short list.
- "Hey Siri, ask my assistant to add 'Draft copy' to Design in Launch due Friday"
  → task appears in Asana, HomePod confirms the action.
- End-to-end latency under Siri's tolerance (target < 8s wall clock).
- Single App Intent, single server endpoint — the agent routes everything.

## Architecture

```
HomePod → Siri (STT) → iPhone App Intent
  → POST /message { query } → FastAPI server
      → Pydantic AI agent loop
          → Agent Engine MCP (Asana, …)
      → { reply }
  → IntentDialog → Siri (TTS) → HomePod
```

Locked choices:
- Monorepo layout: `server/` (Python) and future `ios/` (Xcode).
- **Server framework:** FastAPI.
- **Agent framework:** Pydantic AI.
- **Tool access:** hosted Agent Engine MCP (Airbyte).
- **LLM provider:** Anthropic Claude.
- **Endpoint shape:** single `POST /message`; agent decides whether to read or mutate.

Open choices are tracked as ADRs in [`docs/decisions/`](../decisions/README.md).

## Phases

Each phase is a branch + review checkpoint. Later phases do not assume earlier
phases are locked — we can revisit.

### Phase 0 — Planning & decisions (active)
Resolve the open ADRs in `docs/decisions/` before writing more code. Agree on
phase shape, testing strategy, and success criteria.

### Phase 1 — Server MVP, local only
Scaffold per resolved decisions. Single `/message` endpoint, bearer auth.
Agent wired to Agent Engine MCP. Curl smoke tests for one read ("list projects")
and one write ("create task") against real Asana. Unit tests for endpoint auth,
request validation, and config loading (agent mocked).

**Exit:** two curl commands succeed end-to-end in under 8s; unit tests green.

### Phase 2 — Prompting & behavior
Tune system prompt for voice output (length, tone, mutation confirmation,
error handling). Build a small eval suite (10–20 queries, read + write +
ambiguous) that runs against the real model, separate from unit tests. Decide
whether Haiku holds up or swap to Sonnet.

**Exit:** eval pass rate at an agreed bar.

### Phase 3 — iOS App Intent
Add `ios/` to monorepo. One `AppIntent` with a `String` parameter and an
`AppShortcutsProvider`. Bearer token stored in Keychain on first launch.
XCTest for serialization and Keychain storage (server mocked).

**Exit:** "Hey Siri, ask my assistant …" works on iPhone on-device.

### Phase 4 — HomePod validation
Same iPhone, Personal Requests enabled on HomePod. Run the Phase 2 eval set
by voice. Catch STT mangling of proper nouns; add fuzzy matching in the agent
as needed.

**Exit:** voice path matches curl path for the eval set.

### Phase 5 — Hosting
Pick target (see ADR). Deploy with HTTPS. Secrets moved to chosen store.
CI (GitHub Actions) for lint + test + deploy on merge. Post-deploy smoke test
in CI.

**Exit:** iPhone points at prod URL; voice flow works outside LAN.

### Phase 6 — Polish / stretch
Observability, optional conversation memory for follow-ups, second MCP service
(Calendar, Gmail, Linear) to prove routing holds up at scale. Long-op handling.

## Long-term vision

- Multiple connected services (CRM, support tools, docs) behind the one agent.
- Conversational memory across turns ("what about next week?").
- Proactive notifications (morning digest, deadline nudges) — would require a
  separate scheduled path, not the voice path.
- Possibly extend beyond Siri (Slack bot, web chat) reusing the same server.

## Risks

- **Siri timeout** (~10–30s). Agent loops can blow past it. Mitigation: small
  model, tight tool descriptions, hard server-side timeout with graceful reply.
- **STT mangling** of proper nouns. Mitigation: fuzzy matching in the agent,
  not strict equality.
- **Agent Engine auth model** not yet confirmed. Need to check before Phase 1.
- **HomePod multi-user**: Personal Requests only route to the recognized
  voice's iPhone. Others speaking won't get your data (this is a feature, not
  a bug, but worth knowing).
- **Mutation blast radius**: "delete everything in Design" is a voice command
  away. Consider guardrails (confirmation, no-delete mode, audit log).

## Testing strategy

- **Unit tests** from Phase 1 onward (pytest). Mock the LLM and MCP in unit
  tests — no network, no tokens burned.
- **Eval suite** separate from unit tests, gated behind a pytest marker so it
  only runs when requested. Hits the real model.
- **iOS tests** via XCTest from Phase 3.
- **CI smoke test** post-deploy from Phase 5.
