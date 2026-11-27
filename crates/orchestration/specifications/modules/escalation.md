# Durable human decision request

**ZIP-ORCHESTRATION-ESCALATION-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/escalation.rs`

## Required implementation behavior

Persist scope, digest, evidence, decision role and deadline; stop dependent work. Resume only after exact approved decision and revision check.

## Acceptance

**ZIP-ORCHESTRATION-ESCALATION-T01.** Late answer for changed candidate is rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
