# Knowledge graph and retrieval

**Contract version** 1.0. Master design §71.

## Contract

Nodes and edges carry a stable identity, source revision, byte span where available, derivation version and confidence. A staged generation is queried only after atomic promotion.

## Execution and integration

Retraction removes affected source contributions before generating replacement nodes. Limit traversal by depth and per-query result count and filter access before expanding neighbors. Inferred and observed relationships are distinguishable.

## Verification

Update one file and verify stale relationships disappear and private relations cannot be inferred from counts.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [knowledge crate design](../../crates/knowledge/DESIGN.md)
- [source-analysis crate design](../../crates/source-analysis/DESIGN.md)
- [search crate design](../../crates/search/DESIGN.md)
