# Local evidence catalog

**ZIP-RESEARCH-OFFLINE-LIBRARY-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/offline_library.rs`

## Required implementation behavior

Index approved local objects and metadata with stable cursors; check content digest and access before returning. Never refresh over network automatically.

## Acceptance

**ZIP-RESEARCH-OFFLINE-LIBRARY-T01.** Missing local source reported unavailable under offline policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
