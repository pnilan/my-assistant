---
status: open
started: 2026-04-19
---

# 0004 — Config library

## Context

Server needs to load secrets and settings from environment (and `.env` locally).

## Options

- **pydantic-settings** — typed, validated, integrates with Pydantic models.
- **python-dotenv + os.environ** — minimal; no validation.
- **dynaconf / environs** — heavier frameworks, layered configs.

## Decision

TBD.

## Consequences

TBD.
