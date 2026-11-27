# Mobile client composition

**ZIP-MOBILE-MAIN-001 · v1.0 · Owner:** Mobile maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/mobile/src/main.rs`

## Required implementation behavior

Wire pairing, gateway, credential-reference store and redacted projection with remote review as default. Offline uses cached status only. Approvals require live authenticated scope against current expected digest.

## Acceptance

**ZIP-MOBILE-MAIN-T01.** Offline approval is blocked; cached view is marked stale and cleared after revoked access.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
