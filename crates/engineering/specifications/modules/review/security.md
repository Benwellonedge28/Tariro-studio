# Defensive security review

**ZIP-ENGINEERING-REVIEW-SECURITY-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/review/security.rs`

## Required implementation behavior

Check scope, trust boundary, secret isolation, dependency qualification and negative fixture evidence. Do not infer protection from role/name.

## Acceptance

**ZIP-ENGINEERING-REVIEW-SECURITY-T01.** Missing proof of containment blocks qualified publication.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
