# Repeatability qualification

**ZIP-VERIFICATION-REPRODUCIBILITY-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/reproducibility.rs`

Pin candidate, fixture inputs, commands, seed, toolchain, adapter versions, target platform and relevant environment variables using scoped identities. Record intentional nondeterminism up front. The gate declares exact digest equality or a reviewed comparison algorithm, units and finite tolerance. A comparator consumes validated bounded observations and records its own version. For exact comparison preserve both digests; for tolerance preserve the measured quantities and method. Reject unsupported platform claims or differing input conditions when they invalidate the comparison.

Separate reproduction of a result from reusing a receipt. Each rerun has a distinct attempt identity and independently attributable observation. Timeout, missing input or unavailable tooling blocks. A verified difference beyond the approved tolerance fails. Never choose a favorable result from multiple reruns without the approved attempt policy.

**ZIP-VERIFICATION-REPRODUCIBILITY-T01.** An observed mismatch beyond the reviewed tolerance fails and preserves both input and output identities.
