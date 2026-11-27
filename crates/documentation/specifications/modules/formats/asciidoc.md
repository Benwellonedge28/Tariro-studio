# Asciidoc safe adapter

**ZIP-DOCUMENTATION-FORMATS-ASCIIDOC-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/formats/asciidoc.rs`

## Required implementation behavior

Disable remote includes and executable substitutions by default; parse under bounded qualified adapter with explicit scope for local includes.

## Acceptance

**ZIP-DOCUMENTATION-FORMATS-ASCIIDOC-T01.** A remote include triggers no network and is reported unavailable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
