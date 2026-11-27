# Scoped memory

**Contract version** 1.0. Master design §71.

## Contract

Memory keys belong to organization, workspace, repository or assignment under an explicit visibility policy. Scope and principal checks happen before index lookup. Persistent records include retention expiry, sensitivity, source and tombstone status.

## Execution and integration

Store minimal structured decisions by default. A purge transaction writes tombstones and invalidates query visibility immediately. Background projection cleanup cannot resurrect data from a prior generation.

## Verification

Try cross-workspace retrieval, search after purge before compaction and validate backup restore retention.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [memory crate design](../../crates/memory/DESIGN.md)
- [search crate design](../../crates/search/DESIGN.md)
