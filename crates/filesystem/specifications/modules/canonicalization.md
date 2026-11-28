# Rooted component resolution

**ZIP-FILESYSTEM-CANONICALIZATION-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/canonicalization.rs`

## Boundary and inputs

Resolve validated relative [path](path.md) components starting from an enrolled root handle. Record root generation, parent and target identity, object type and access mode through trusted platform proof. Canonical display strings are for diagnostics. They cannot authorize an open.

## Behavior and failure handling

Validate component identity under qualified handle-relative resolution and link policy. Revalidate exact directory or target bindings at the actual effect boundary, including after an ancestor changes. If the adapter cannot prove the required scope and object type under concurrent substitution, fail closed. Return no broad reusable host handle.

## Acceptance

**ZIP-FILESYSTEM-CANONICALIZATION-T01.** Change a synthetic ancestor between preliminary observation and controlled access. Verify no access outside the approved root and no verified identity receipt for the stale binding.
