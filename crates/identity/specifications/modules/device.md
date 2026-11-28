# Paired device identity

**ZIP-IDENTITY-DEVICE-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/device.rs`

## Boundary and inputs

Bind a typed device ID, paired workspace, authorized owner principal, qualified key reference, pairing purpose and accepted pairing receipt. Verify proof binds the exact enrolled key and challenge or qualified channel before activation. Key or device labels entered by a caller do not establish possession.

## Behavior and failure handling

Claim single-use pairing approval under the owning revision-checked enrollment path and persist generation and original receipt. A device's enrollment does not transfer the owner's role. Rotation updates proof reference under a separately authorized transition. Revoke or retire through the live generation fence and preserve old provenance.

## Acceptance

**ZIP-IDENTITY-DEVICE-T01.** Replay a synthetic pairing approval with a different enrolled device key, then replay the accepted command. Verify the first denies, the second does not create another enrollment, and old generation is fenced after revoke.
