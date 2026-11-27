# Safe Rust implementation standard

**ZIP-IMPL-001 · v1.0 · Owner:** Workspace maintainers. **Maturity:** D4 candidate.

Every first-party crate root declares `#![forbid(unsafe_code)]`. The workspace declares `[workspace.lints.rust]` with `unsafe_code = "forbid"` and each member uses `[lints]` with `workspace = true`. Cover libraries, binaries, tests, benches, examples and build scripts. Generated Rust is subject to the same rule. Keep transitive native/unsafe code review in [DEPENDENCIES.md](DEPENDENCIES.md).

| Area | Implementation rule | Rejection evidence |
| --- | --- | --- |
| Numeric operations | Checked conversion and arithmetic at bounds; typed bytes, tokens, count and elapsed time | Overflow, truncation or wrapped counters |
| Parsing | Validate before construction and allocation; charge through an admitted budget | Arbitrary input triggers unchecked allocation |
| Errors | Propagate typed error or record explicitly handled outcome | Ignored required failures, fabricated pass or user-triggerable panic |
| Concurrency | Own every task in a supervisor and check termination | Detached workers, unbounded queues or lost shutdown obligations |
| Secrets | Pass opaque references; resolve in the approved adapter | Secret canary reaches logs, prompts, errors or persisted artifacts |
| Platform | Probe supported controls and fail closed for unavailable mandatory enforcement | Degraded isolation presented as full capability |

Implement contract test fixtures beside each crate. CI must check workspace membership and lint inheritance, run locked feature matrices, and reject a synthetic first-party unsafe block. Do not add a default or fixed ceiling for an operational resource outside the rules in [LIMITS_POLICY.md](LIMITS_POLICY.md).
