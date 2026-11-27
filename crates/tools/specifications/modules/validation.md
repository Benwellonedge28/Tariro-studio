# Pre-effect request validation

**ZIP-TOOLS-VALIDATION-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/validation.rs`

## Required implementation behavior

Validate tool ID, arguments, descriptor integrity, declared effect and available policy/lease. Preserve precise classification for failed checks.

## Acceptance

**ZIP-TOOLS-VALIDATION-T01.** Scope mismatch stops before adapter execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
