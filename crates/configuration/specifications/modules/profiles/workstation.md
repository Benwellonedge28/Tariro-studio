# Workstation profile rules

**ZIP-CONFIGURATION-PROFILES-WORKSTATION-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/workstation.rs`

## Required implementation behavior

Use capability-aware best-fit local placement. Compute accelerator budgets by device and do not combine disjoint VRAM pools unless the adapter supports qualified sharding.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-WORKSTATION-T01.** Reject a one-device model larger than every individual device even when summed VRAM is sufficient.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
