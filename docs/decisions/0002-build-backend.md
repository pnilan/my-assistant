---
status: open
started: 2026-04-19
---

# 0002 — Build backend

## Context

`pyproject.toml` needs a build backend for packaging. Not user-facing; the
main axis is ecosystem familiarity and `uv` compatibility.

## Options

- **hatchling** — modern, fast, minimal config. Current default in many templates.
- **setuptools** — universally compatible; heavier legacy.
- **uv_build** — Astral's own backend; newest, tight uv integration.
- **flit-core** — minimal, good for pure-Python libraries.

## Decision

TBD.

## Consequences

TBD.
