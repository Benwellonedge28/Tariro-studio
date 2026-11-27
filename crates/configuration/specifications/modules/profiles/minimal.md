# Minimal profile rules

**ZIP-CONFIGURATION-PROFILES-MINIMAL-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/minimal.rs`

## Required implementation behavior

Prefer serial deterministic tasks. Explicitly permit zero loaded generation models. Do not enable remote inference by profile selection. Enforce all normal policy caps against discovered capacity.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-MINIMAL-T01.** Generation is denied under zero-slot profile even with available RAM; deterministic local work remains admissible.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
