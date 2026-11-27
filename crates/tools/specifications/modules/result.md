# Verified result representation

**ZIP-TOOLS-RESULT-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/result.rs`

## Required implementation behavior

Return confirmed, failed, cancelled or unresolved with actual evidence refs and optional continuation. Untrusted output cannot imply authority or completion.

## Acceptance

**ZIP-TOOLS-RESULT-T01.** Adapter message claiming success without matching receipt remains unverified.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
