# Foundation contract fixtures

**Maturity:** D4 candidate.

Run deterministic unit and property fixtures for identifier canonicalization, digest representation, private-field validation, numeric overflow and compatibility negotiation. Cover both acceptance and denials for every constructor. Assert denied constructors preserve caller state and allocate no storage where the contract promises it.

Run cancellation with a deterministic race harness: poll before cancel, cancel before first poll, concurrent cancels, cancellation after waiter drop, waker replacement, and waker re-entry outside the lock. Record maximum elapsed time separately under a qualified runtime profile. Every fixture records the seed and failing interleaving when reproducible.

Foundation is platform-neutral at the interface level. Test representative targets under the pinned toolchain and locked feature graph. Wire adapters own cross-process, durable data, and provider integration fixtures. Follow [test evidence requirements](../../../TESTING_STANDARD.md).
