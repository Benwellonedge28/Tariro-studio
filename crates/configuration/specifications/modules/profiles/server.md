# Server profile rules

**ZIP-CONFIGURATION-PROFILES-SERVER-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/server.rs`

## Required implementation behavior

Prefer headless scheduling and audit retention. Local binding remains default. Service identities and remote listener require distinct validated policy entries.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-SERVER-T01.** Enabling the server profile alone creates no non-loopback listener.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
