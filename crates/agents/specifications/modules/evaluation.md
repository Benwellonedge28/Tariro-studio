# Agent outcome qualification

**ZIP-AGENTS-EVALUATION-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/evaluation.rs`

## Required implementation behavior

Compare output to exact requirements, observed evidence and independent checks. Separate quality scores from acceptance.

## Acceptance

**ZIP-AGENTS-EVALUATION-T01.** High model confidence cannot pass a missing mandatory check.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
