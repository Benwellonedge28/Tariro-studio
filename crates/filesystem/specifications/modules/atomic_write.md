# Conditional publication

**ZIP-FILESYSTEM-ATOMIC-WRITE-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/atomic_write.rs`

## Boundary and inputs

Accept an approved write intent naming target bound to a scoped root, verified expected revision and digest or explicit expected absence, new immutable bytes, finite limits and stable operation identity. Stage a verified private object in the destination directory and finish the adapter's required object sync before publication. Require qualified capacity, durability and conditional-replacement evidence.

## Behavior and failure handling

Before replacing, revalidate live authorization and root/parent/target bindings under the backend's qualified conditional-write boundary. A cooperative lock alone cannot guard external writers. If the backend cannot fence the required preimage, deny. Record intent before replacement. Distinguish definite nonapplication, visible replacement awaiting durability, and unknown outcome. Reconcile ambiguous completion before retry. Commit success only after required containing-directory durability or its qualified equivalent, and a matching effect receipt.

## Acceptance

**ZIP-FILESYSTEM-ATOMIC-WRITE-T01.** Race two writers from the same preimage and a third change outside their lock. At most one matching replace commits. A failed rename leaves the preimage intact, and a lost reply invokes reconciliation without another blind replace.
