# Governance facade

**ZIP-GOVERNANCE-LIB-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/lib.rs`

## Required implementation behavior

Expose policy snapshots, decision outcomes, approvals and independently enforced effect guards. Registry and storage ports are injected. No globally trusted policy default.

## Acceptance

**ZIP-GOVERNANCE-LIB-T01.** Missing policy yields deny from public facade.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
