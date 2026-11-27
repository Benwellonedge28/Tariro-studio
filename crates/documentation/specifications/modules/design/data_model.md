# Data model specification

**ZIP-DOCUMENTATION-DESIGN-DATA-MODEL-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/design/data_model.rs`

## Required implementation behavior

Declare exact fields, ownership, validation, keying, portability and versioned wire representation. Explain absence and null separately where relevant.

## Acceptance

**ZIP-DOCUMENTATION-DESIGN-DATA-MODEL-T01.** Missing durable record schema is flagged before implementation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
