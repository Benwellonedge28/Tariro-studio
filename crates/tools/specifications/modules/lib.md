# Typed tool service facade

**ZIP-TOOLS-LIB-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/lib.rs`

## Required implementation behavior

Expose descriptor, registry, invocation and result contracts. Wire effects through governance and sandbox; no library import invokes a tool.

## Acceptance

**ZIP-TOOLS-LIB-T01.** Facade-only consumer performs no network or process effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
