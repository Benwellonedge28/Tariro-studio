# Paired device identity

**ZIP-IDENTITY-DEVICE-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/device.rs`

## Required implementation behavior

Bind device ID, approved key reference, workspace and scope to explicit pairing receipt. Revoke by advancing generation.

## Acceptance

**ZIP-IDENTITY-DEVICE-T01.** A copied pairing token for a different device fails proof.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
