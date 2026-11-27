# Evidence references and immutability

**ZIP-ASSIGNMENTS-EVIDENCE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/evidence.rs`

## Required implementation behavior

Persist verifier ID/version, requirement, reviewed digest, observed artifact ref and verdict as immutable linked evidence. Verify scope on insertion and fetch. Never accept agent prose as an observation.

## Acceptance

**ZIP-ASSIGNMENTS-EVIDENCE-T01.** Wrong candidate or missing reference cannot satisfy completion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
