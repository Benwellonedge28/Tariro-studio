# Public configuration boundary

**ZIP-CONFIGURATION-LIB-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/lib.rs`

## Required implementation behavior

Declare the planned modules and expose TypedConfig and ResolvedConfig through schema; no global loader or filesystem access on import.

## Acceptance

**ZIP-CONFIGURATION-LIB-T01.** A downstream consumer compiles using configuration types without network or startup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
