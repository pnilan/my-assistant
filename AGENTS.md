# my-assistant

A voice-controlled personal assistant: Siri (HomePod/iPhone) → App Intent → FastAPI server → Pydantic AI agent → Agent Engine MCP → business systems (Asana first).

## Start here

- **Plan**: [`docs/plans/`](docs/plans/README.md). Start with [`00-overview.md`](docs/plans/00-overview.md).
- **Decisions**: [`docs/decisions/`](docs/decisions/README.md) — ADR-style, one file per resolved or in-flight decision.

Per-phase detailed plans are written when a phase becomes active. Never delete
historical plans or decisions — mark them `done` or `abandoned` and leave in place.

## Repo layout

```
my-assistant/
├── AGENTS.md                 this file
├── CLAUDE.md                 symlink → AGENTS.md
├── docs/
│   ├── plans/                living plans, per-phase
│   └── decisions/            ADRs
└── server/                   Python backend (FastAPI + Pydantic AI)
    ├── src/my_assistant/
    ├── pyproject.toml
    └── .env.example
# ios/ added in Phase 3
```

## Locked choices

See `docs/plans/00-overview.md` for full context. Summary:

- Monorepo (`server/`, future `ios/`).
- FastAPI server.
- Pydantic AI agent framework.
- Hosted Agent Engine MCP as the tool layer.
- Anthropic Claude as the LLM provider.
- Single `POST /message` endpoint — the agent decides whether to read or mutate.

## Open decisions

Tracked in [`docs/decisions/`](docs/decisions/README.md). Do not silently pick
infrastructure or dependency choices — surface options with tradeoffs and
resolve them as ADRs first.

## Working conventions

- **Feature branches** for any change. Do not work on `main`.
- **Plan before building.** If a phase's detailed plan doesn't exist yet,
  write it (under `docs/plans/NN-<slug>.md`) before writing code for that phase.
- **Tests** from Phase 1 onward. Unit tests mock the LLM and MCP — no tokens
  burned in unit runs. Eval suite is separate and opt-in.
- **Voice-shaped output**: the assistant's replies are spoken aloud. Keep them
  short, no markdown, no URLs, confirm mutations in plain English.

## Running the server (once decisions resolved)

```
cd server
cp .env.example .env   # fill in
uv sync
uv run uvicorn my_assistant.main:app --reload
```

(ASGI server command will change if ADR 0001 picks something other than uvicorn.)
