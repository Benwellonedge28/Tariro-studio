# Cross-artifact consistency gate

**ZIP-VERIFICATION-QUALITY-CONSISTENCY-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/quality/consistency.rs`

## Required implementation behavior

Compare authority, schema, revision and requirement across contract, artifact and evidence. Record concrete conflicting values and owners.

## Acceptance

**ZIP-VERIFICATION-QUALITY-CONSISTENCY-T01.** Conflicting normative budget values block review.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
