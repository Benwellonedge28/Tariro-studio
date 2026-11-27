# Distributed compute

**Contract version** 1.0. Master design §71.

## Contract

Node advertisements declare authenticated node identity, platform, capability version, capacity, trust and locality. Leases carry attempt epoch, expiry and artifact manifest. Owner node is authoritative for accepted state.

## Execution and integration

Only authorized candidate nodes receive scoped data. Coordinator verifies artifacts and evidence before accepting a worker result. On partition, fence prior lease before reissuing. Use explicit conflict states.

## Verification

Multiworker fixture observes partition, stale worker result, incorrect artifact digest and resource overcommit.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [distributed crate design](../../crates/distributed/DESIGN.md)
- [synchronization crate design](../../crates/synchronization/DESIGN.md)
- [scheduler crate design](../../crates/scheduler/DESIGN.md)
