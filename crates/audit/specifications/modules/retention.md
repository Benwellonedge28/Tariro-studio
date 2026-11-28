# Evidence-preserving reclamation

**ZIP-AUDIT-RETENTION-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/retention.rs`

## Boundary and inputs

Plan only bounded contiguous prefix reclamation in one workspace. Use validated age and size policy, scoped deletion authority, current chain head, verified active pins and applicable retention obligations. Select a cutoff only where every record in the proposed prefix is eligible. Establish a verified, durable anchor for the last removed sequence and digest before any physical removal.

## Behavior and failure handling

Validate required signing or independent anchor trust, and preserve the separately trusted high-water history. Recheck pinned evidence and expected generation under the owning transaction. Atomically publish the anchor, retained boundary and earliest valid cursor with logical removal. Physical cleanup follows the Storage policy and may be resumed by exact identity. Do not reset the head. A failure preserves references, or leaves an explicitly recoverable cleanup.

## Acceptance

**ZIP-AUDIT-RETENTION-T01.** Pin an interior release record and verify reclamation cannot cross it. Remove the pin under authorized policy, prune a qualified prefix, and verify current reads connect to the anchor while old cursors expire atomically.
