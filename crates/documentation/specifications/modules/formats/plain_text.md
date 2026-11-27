# Plain text delivery

**ZIP-DOCUMENTATION-FORMATS-PLAIN-TEXT-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/formats/plain_text.rs`

## Required implementation behavior

Normalize documented newline rules; preserve UTF-8 and explicit truncation status under admitted limit. Escape control codes at presentation boundary.

## Acceptance

**ZIP-DOCUMENTATION-FORMATS-PLAIN-TEXT-T01.** A terminal control sequence does not execute on display.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
