# Durable emergency stop

**ZIP-GOVERNANCE-OVERSIGHT-EMERGENCY-STOP-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/oversight/emergency_stop.rs`

## Required implementation behavior

Commit stop flag plus fencing epoch, close intake and request cleanup. Resume is a separate authenticated transition; earlier grants remain evaluated under current epoch.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-EMERGENCY-STOP-T01.** Restart during stop refuses new effects and reconciles in-flight receipts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
