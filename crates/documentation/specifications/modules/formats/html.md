# HTML output adapter

**ZIP-DOCUMENTATION-FORMATS-HTML-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/formats/html.rs`

## Required implementation behavior

Serialize sanitized content under safe allowed elements; never execute embedded scripts in source or generated preview. Do not read subresources by default.

## Acceptance

**ZIP-DOCUMENTATION-FORMATS-HTML-T01.** An embedded script is removed or escaped consistently by policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
