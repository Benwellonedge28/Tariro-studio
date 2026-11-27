# Effective wall-time deadline

**ZIP-TERMINAL-TIMEOUT-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/timeout.rs`

## Required implementation behavior

Use earliest monotonic request, lease and policy deadline and signal supervisor on expiry. Keep outcome distinct from explicit cancel and cleanup clock.

## Acceptance

**ZIP-TERMINAL-TIMEOUT-T01.** Changing host UTC clock cannot extend execution time.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
