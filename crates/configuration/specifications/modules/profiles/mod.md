# Named profile dispatch

**ZIP-CONFIGURATION-PROFILES-MOD-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/mod.rs`

## Required implementation behavior

Profile selection maps stable IDs to validated profile definitions. Resolve explicit profile values versus derivation keys; the same key may occur in only one category. No host-memory heuristics select security posture.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-MOD-T01.** Unknown profile name and duplicate derivation/override are rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
