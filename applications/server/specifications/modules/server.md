# Bounded listener lifecycle

**ZIP-SERVER-SERVER-001 · v1.0 · Owner:** Server maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/server/src/server.rs`

## Required implementation behavior

Admit connections/requests, apply validated size and deadline before decode, route typed operations and record replies. Shutdown stops intake, drains with bounded grace and reconciles unknown status.

## Acceptance

**ZIP-SERVER-SERVER-T01.** Concurrent requests above admission are denied and interrupted replies remain reconcilable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
