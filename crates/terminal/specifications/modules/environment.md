# Explicit environment construction

**ZIP-TERMINAL-ENVIRONMENT-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/environment.rs`

## Required implementation behavior

Build only allowlisted names and validated values; no inheritance from process secrets or proxy defaults. Resolve opaque credential through qualified effect-local adapter when authorized.

## Acceptance

**ZIP-TERMINAL-ENVIRONMENT-T01.** Injected parent environment canary absent in child.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
