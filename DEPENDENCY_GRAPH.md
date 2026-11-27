# Workspace dependency graph

**ZIP-DEP-001 · v1.0 · Owner:** Workspace architecture maintainers. **Maturity:** D4 candidate for the pinned documented graph.

The [graph](contracts/dependencies/graph.json) contains 48 documented crate packages. Architecture references may also describe applications and adapters, which do not add crate nodes until separately authorized. Each edge is a permitted first-party Cargo dependency, with explicit optional and target semantics. An edge being permitted does not require it to be present in a given release.

Validation order:

1. Validate the graph [schema](contracts/schemas/dependency-graph.schema.json), node uniqueness and resolvable edge endpoints.
2. Reject self-edges and cycles, including the union of optional or target-specific first-party edges. Sort ready nodes by identifier to produce deterministic construction order.
3. Compare every realized first-party Cargo edge against the canonical graph using Cargo metadata for declared release target/feature combinations. Reject undeclared or unexpectedly activated edges.
4. Verify that every node names its own design contract. Treat external dependencies separately under [DEPENDENCIES.md](DEPENDENCIES.md).
5. Emit the exact missing/forbidden edge, cycle path or unresolved component. Verification and testing communicate through injected runner contracts to avoid cyclic dependencies.

The graph bootstraps from [the current dependency rules](specifications/0100-architecture/dependency-rules.md). Documented edges are unconditional in this revision. A future optional/target edge needs an explicit feature and/or target predicate, an owner and a cross-target fixture.
