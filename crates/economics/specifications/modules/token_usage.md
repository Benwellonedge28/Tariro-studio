# Token usage attribution

**ZIP-ECONOMICS-TOKEN-USAGE-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/token_usage.rs`

## Required implementation behavior

Bind requested and observed input/output to model, tokenizer, provider and attempt. Preserve source and count uncertainty without conflating units.

## Acceptance

**ZIP-ECONOMICS-TOKEN-USAGE-T01.** Estimated tokens do not overwrite confirmed provider measure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
