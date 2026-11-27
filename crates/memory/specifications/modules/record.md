# Versioned memory record

**ZIP-MEMORY-RECORD-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/record.rs`

## Required implementation behavior

Store typed scope/owner, kind, content digest, evidence refs, sensitivity, creation and retention policy. Treat payload as untrusted.

## Acceptance

**ZIP-MEMORY-RECORD-T01.** Unknown schema or classification prevents activation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
