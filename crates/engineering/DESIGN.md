# Engineering crate design

**Contract version** 1.0. Master design §32. Planned implementation.

## Responsibility and dependencies

Bind proposed changes to requirement IDs and reviewed base. Apply in isolated staging, compute diff, handle conflicts without implicit merges, verify exact final tree.

First-party dependencies: [foundation](../foundation/DESIGN.md), [assignments](../assignments/DESIGN.md), [repository](../repository/DESIGN.md), [verification](../verification/DESIGN.md)

- [Engineering](../../specifications/1600-engineering/engineering.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `plan_change(requirements)`
- `stage_patch(patch)`
- `verify_candidate(candidate)`

Record families: ChangePlan, PatchSet, impact map and verification record. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ChangePlan { requirement_ids, reviewed_base, permitted_paths, checks }`
- `PatchSet { preimages, operations, digest }`
- `Candidate { tree_digest, plan_digest, validation_refs }`

- `stage_patch(plan: ChangePlan, patch: PatchSet, lease: WorktreeLease) -> Result<Candidate>`

## Failure, safety and resource limits

Cap patch paths and bytes to grant limits. Privileged changes require narrower operation authority. No publication on verification failure.

- `PatchConflict`
- `ScopeDenied`
- `VerificationFailed`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/engineering/src/
├── lib.rs
├── error.rs
├── requirements/
│   ├── mod.rs
│   ├── extraction.rs
│   ├── specification.rs
│   ├── traceability.rs
│   └── validation.rs
├── architecture/
│   ├── mod.rs
│   ├── system.rs
│   ├── component.rs
│   ├── interfaces.rs
│   ├── dependencies.rs
│   ├── decisions.rs
│   └── validation.rs
├── implementation/
│   ├── mod.rs
│   ├── generation.rs
│   ├── editing.rs
│   ├── patching.rs
│   ├── integration.rs
│   └── validation.rs
├── refactoring/
│   ├── mod.rs
│   ├── rename.rs
│   ├── extraction.rs
│   ├── restructuring.rs
│   └── equivalence.rs
├── optimization/
│   ├── mod.rs
│   ├── performance.rs
│   ├── memory.rs
│   ├── concurrency.rs
│   └── algorithms.rs
├── review/
│   ├── mod.rs
│   ├── correctness.rs
│   ├── maintainability.rs
│   ├── security.rs
│   └── compatibility.rs
└── traceability.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test conflicting edits, out-of-scope files and evidence invalidation after changes.
