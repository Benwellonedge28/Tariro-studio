# Provider adapter registry

**ZIP-INTELLIGENCE-PROVIDERS-MOD-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/providers/mod.rs`

## Required implementation behavior

Resolve negotiated approved provider kind with typed contracts. Unsupported kind remains unavailable without fallback.

## Acceptance

**ZIP-INTELLIGENCE-PROVIDERS-MOD-T01.** Choosing nonexistent provider leaves other routes untouched.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
