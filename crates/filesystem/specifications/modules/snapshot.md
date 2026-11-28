# Immutable read manifest

**ZIP-FILESYSTEM-SNAPSHOT-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/snapshot.rs`

## Boundary and inputs

Pin a bounded root generation and verified consistent enumeration basis. Store a deterministic mapping of authorized relative paths, typed identity, regular-file digests and stream lengths. Preserve each immutable value and comparable preimage revision used by callers. Snapshot creation and later reads require their own authorization.

## Behavior and failure handling

For a backend without trusted snapshot or equivalent consistency proof, detect changes during verification and report incomplete or changed state. Never label a mixed traversal verified. Keep ordering and cursor state separate from eligibility. Finish only after all requested paths and root generation reconcile.

## Acceptance

**ZIP-FILESYSTEM-SNAPSHOT-T01.** Modify one file partway through creation and verify a changed-state result. Compare two unordered enumerations of identical bytes and identities and verify the same canonical manifest.
