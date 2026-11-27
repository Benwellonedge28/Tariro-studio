# Qualified prompt template adapter

**ZIP-CONTEXT-TEMPLATE-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/template.rs`

## Required implementation behavior

Pin template identity and tokenizer, validate inputs and escape embedded data. Render bounded bytes without arbitrary executable evaluation.

## Acceptance

**ZIP-CONTEXT-TEMPLATE-T01.** Untrusted interpolation cannot create a trusted-role message.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
