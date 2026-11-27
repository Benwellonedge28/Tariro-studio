# Audience-bound session

**ZIP-IDENTITY-SESSION-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/session.rs`

## Required implementation behavior

Store opaque session ID, actor, workspace, audience, expiry and epoch, without raw bearer material. Resolve only if current, active and correctly bound.

## Acceptance

**ZIP-IDENTITY-SESSION-T01.** At exact expiry or wrong audience, resolution fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
