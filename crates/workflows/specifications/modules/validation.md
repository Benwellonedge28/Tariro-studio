# Workflow structural and policy checks

**ZIP-WORKFLOWS-VALIDATION-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/validation.rs`

## Required implementation behavior

Reject missing nodes, cycles, invalid variables, excess depth/steps, unsupported capabilities and impossible mandatory requirements before schedule.

## Acceptance

**ZIP-WORKFLOWS-VALIDATION-T01.** Static bounds reject excess step expansion without starting a child.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
