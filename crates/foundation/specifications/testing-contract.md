# Foundation contract fixtures

**Maturity:** D4 candidate.

Run deterministic unit and property fixtures for identifier canonicalization, digest representation, private-field validation, numeric overflow and compatibility negotiation. Cover both acceptance and denials for every constructor. Assert denied constructors preserve caller state and allocate no storage where the contract promises it.

Run cancellation with a deterministic race harness: poll before cancel, cancel before first poll, concurrent cancels, cancellation after waiter drop, waker replacement, and waker re-entry outside the lock. Record maximum elapsed time separately under a qualified runtime profile. Every fixture records the seed and failing interleaving when reproducible.

Foundation is platform-neutral at the interface level. Test representative targets under the pinned toolchain and locked feature graph. Wire adapters own cross-process, durable data, and provider integration fixtures. Follow [test evidence requirements](../../../TESTING_STANDARD.md).

## Test oracle and reporting

Use the [fixture catalog](../../../contracts/acceptance/foundation/fixtures.json) as the stable source for case IDs, input procedures and required observations. It covers every acceptance ID in the Foundation file contracts. Each implementation fixture must publish exactly one result per case and attach actual output, seed or schedule, tested commit and supported target. Record compile failures only when the diagnostic identifies the intended capability or type boundary rather than an unrelated syntax error.

Use a qualified external allocation probe for allocation assertions. Keep it outside first-party code or use a dependency whose unsafe exposure was explicitly reviewed. Use deterministic barriers and safe waker fixtures for concurrency; a timeout indicates failure or incomplete observation, not success. Run property seeds under a finite reviewed test profile and record the seed and minimized counterexample.

The catalog remains specified, with no Rust execution evidence attached. Review and implementation are still required. A successful static link or fixture-coverage check is evidence about the documentation and inventory only.
