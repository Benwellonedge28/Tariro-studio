# Ordered owned write locks

**ZIP-FILESYSTEM-LOCKING-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/locking.rs`

## Boundary and inputs

Acquire cooperating writer locks by canonical workspace, root and target keys, sorted in one stable order with duplicates removed. Validate scoped generation and current operation before obtaining the set. Use a finite wait and cancellable bounded waiter envelope.

## Behavior and failure handling

If acquisition fails, release only acquired ownership in reverse order. A lock protects cooperating writers and supplies no proof against unrelated actors. Combine it with qualified root identity and expected-target checks at the replace boundary. A stale lease cannot unlock a replacement owner's state.

## Acceptance

**ZIP-FILESYSTEM-LOCKING-T01.** Run two transactions requesting the same target set in opposite orders. Verify no deadlock or partial publication. Cancel a partially acquired attempt and confirm all and only its locks are released.
