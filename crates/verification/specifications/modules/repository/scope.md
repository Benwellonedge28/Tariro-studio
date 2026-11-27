# Change authorization proof

**ZIP-VERIFICATION-REPOSITORY-SCOPE-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/repository/scope.rs`

## Required implementation behavior

Match effective allowed root and path, operation and reviewed grant against exact diff. Check both paths of rename and special-file restrictions.

## Acceptance

**ZIP-VERIFICATION-REPOSITORY-SCOPE-T01.** Allowed source renamed to disallowed target fails immediately.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
