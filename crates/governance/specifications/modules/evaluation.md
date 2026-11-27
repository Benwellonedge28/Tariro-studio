# Policy regression and dry-run comparison

**ZIP-GOVERNANCE-EVALUATION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/evaluation.rs`

## Required implementation behavior

Evaluate candidate policy against pinned synthetic scenarios without effects. Report exact decision changes, including any newly allowed scope and unresolved mandatory inputs.

## Acceptance

**ZIP-GOVERNANCE-EVALUATION-T01.** An intended tightening that widens one path appears as a failed qualification case.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
