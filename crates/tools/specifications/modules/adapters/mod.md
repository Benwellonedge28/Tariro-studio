# Adapter interface selection

**ZIP-TOOLS-ADAPTERS-MOD-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/adapters/mod.rs`

## Required implementation behavior

Resolve native/process/HTTP/MCP/plugin adapter from qualified descriptor and version. Unsupported stays unavailable.

## Acceptance

**ZIP-TOOLS-ADAPTERS-MOD-T01.** No fallback to arbitrary process for unsupported tool.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
