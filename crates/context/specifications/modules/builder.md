# Deterministic assembly pipeline

**ZIP-CONTEXT-BUILDER-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/builder.rs`

## Required implementation behavior

Reserve mandatory policy and instructions first, then evidence and ranked eligible snippets. Count tokens with exact tokenizer and reject oversized mandatory context.

## Acceptance

**ZIP-CONTEXT-BUILDER-T01.** Equal tied inputs produce identical selection independent of retrieval order.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
