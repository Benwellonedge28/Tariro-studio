# Document structural and semantic gate

**ZIP-DOCUMENTATION-VALIDATION-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/validation.rs`

## Required implementation behavior

Check required sections, links, claims, role and applicable conventions. Separate mechanical validation from independent review. Missing mandatory evidence blocks.

## Acceptance

**ZIP-DOCUMENTATION-VALIDATION-T01.** Structurally valid Markdown with false source claim cannot pass.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
