# Deterministic workflow plan

**ZIP-WORKFLOWS-COMPILER-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/compiler.rs`

```rust
pub fn compile(
    definition: &crate::definition::WorkflowDefinition,
    capabilities: &crate::registry::CapabilitySnapshot,
    limits: &CompileLimits,
) -> Result<CompiledGraph, crate::error::WorkflowError>;
```

The compiler borrows immutable inputs and returns an owned graph. `CompileLimits` carries the resolved positive step and nesting caps and admitted byte and decoding budgets. The result stores schema and compiler versions, workflow ID and definition revision, capability snapshot digest, canonical nodes and edges, typed bindings, effect classifications, resolved execution limits and plan digest. Owning modules provide approved capability snapshots and normalized definition types. There are no mutable adapters, network calls or effect permits during compilation.

1. Validate syntax-derived types, identifier uniqueness and capability availability. Validate the unexpanded scoped graph and reject cycles before expansion.
2. Compute checked expansion counts for stages, leaves and repeated scopes. Compare with policy before allocating the expanded graph. Lower each scope into normalized node identities using [looping](looping.md).
3. Resolve every input and dependency to exactly one node and output or an explicitly typed optional input. Compute [dependency order](dependency.md). Reject inconsistent binding, unsupported effects and unowned shared writes.
4. Seal the semantic plan with a versioned canonical encoding. Sort nodes by canonical identity and edges by endpoint pair and edge kind. Sort named bindings and map entries by UTF-8 bytes. Preserve array order only where the definition declares it semantically significant. Use fixed-width big-endian integers, explicit type tags and length-prefix byte fields. A changed version, effective limit or capability binding changes the plan digest. Preserve the exact decoded source digest separately for provenance. Golden vectors and type registry qualification remain required before independent approval.

**ZIP-WORKFLOWS-COMPILER-T01.** Permute independent definitions and binding-map order without changing the semantic graph. Obtain the same plan digest and stable topological order. Change an edge or capability version and obtain a different plan digest.
