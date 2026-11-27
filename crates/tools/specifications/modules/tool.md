# Tool descriptor and authority request

**ZIP-TOOLS-TOOL-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/tool.rs`

## Required implementation behavior

Bind name/version, schema, effect class, limit declarations and adapter identity. Descriptors provide capability metadata; identity grant is separate.

## Acceptance

**ZIP-TOOLS-TOOL-T01.** A tool cannot gain an effect by changing its displayed name.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
