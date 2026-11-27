# Atomic shared output accounting

**ZIP-TERMINAL-OUTPUT-LIMITS-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/output_limits.rs`

## Required implementation behavior

Coordinate stdout and stderr with checked reservation, capture accepted prefix and typed overflow and stop or truncate only as policy defines.

## Acceptance

**ZIP-TERMINAL-OUTPUT-LIMITS-T01.** Concurrent stream writes cannot both spend the final available byte.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
