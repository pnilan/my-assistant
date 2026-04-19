---
status: open
started: 2026-04-19
---

# 0010 — Secrets management

## Context

Anthropic API key, Agent Engine token, bearer token, eventual Asana OAuth
refresh token all need to live somewhere.

## Options

- **`.env` on host** — simplest; fine for solo use behind a firewall.
- **Doppler / 1Password Connect** — centralized secrets with rotation.
- **Cloud KMS** (AWS SSM, GCP Secret Manager) — enterprise-grade, more setup.

## Decision

TBD.

## Consequences

TBD.
