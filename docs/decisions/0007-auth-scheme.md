---
status: open
started: 2026-04-19
---

# 0007 — Auth scheme (iOS ↔ server)

## Context

The iOS App Intent posts to the server from off-network. The endpoint must
not be open to the internet.

## Options

- **Shared bearer token** in iOS Keychain — simplest for single-user.
- **Sign in with Apple** — real identity, useful if ever multi-user.
- **Signed JWTs** — time-limited tokens, more complex.
- **mTLS** — client cert on device; most secure, most ops overhead.

## Decision

TBD.

## Consequences

TBD.
