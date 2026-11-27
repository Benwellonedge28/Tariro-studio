# Repository failure vocabulary

**ZIP-REPOSITORY-ERROR-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/error.rs`

## Required implementation behavior

Classify InvalidRef, InstructionsIncomplete, ScopeDenied, Conflict, StaleRevision, ProviderUnavailable, UnknownEffect, VerificationMismatch and Cancelled. Unknown remote outcome never claims rollback.

## Acceptance

**ZIP-REPOSITORY-ERROR-T01.** Timeout following possible push remains unknown until inspected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
