# Bounded workflow decode

**ZIP-WORKFLOWS-PARSER-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/parser.rs`

## Required implementation behavior

Charge document bytes, reject duplicate keys and unsupported schema, produce typed immutable definition with origin and digest. No shell or template expression evaluation.

## Acceptance

**ZIP-WORKFLOWS-PARSER-T01.** Malformed input yields typed parse failure before compilation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
