# Actual build checks

**ZIP-COMPILATION-VERIFICATION-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/verification.rs`

## Required implementation behavior

Bind qualified tool output, exit and verified artifact manifest to exact input and compare required checks. Record unsupported platform separately.

## Acceptance

**ZIP-COMPILATION-VERIFICATION-T01.** Filename alone never constitutes a verified build output.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
