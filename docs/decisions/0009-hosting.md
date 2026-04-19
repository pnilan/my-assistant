---
status: open
started: 2026-04-19
---

# 0009 — Hosting target

## Context

Phase 5 deploys the server behind HTTPS so the iPhone can reach it off-LAN.
Needs to be cheap, fast to iterate on, and low-ops for a solo project.

## Options

- **Fly.io** — good latency, generous free tier, simple Dockerfile deploy.
- **Railway** — easiest onboarding, higher cost at scale.
- **Render** — straightforward, slower cold starts on free tier.
- **Small VPS** (Hetzner, DO) — cheapest at scale, manual ops.
- **Home Mac + Cloudflare Tunnel** — zero cost, depends on home uptime.

## Decision

TBD.

## Consequences

TBD.

## Related

- Phase 5 in [`plans/00-overview.md`](../plans/00-overview.md).
