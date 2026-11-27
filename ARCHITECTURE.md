# System architecture

Zipporah is a local-first Safe Rust runtime. CLI, Studio, Server, Mobile and SDK are clients of the same governed command gateway. Applications own presentation and transport. The gateway authenticates requests, resolves the workspace, evaluates policy and passes typed requests to application services.

| Boundary | Owns | Integrates through |
| --- | --- | --- |
| Foundation | Identifiers, bounded quantities, versions and errors | Value types only |
| Infrastructure | Persistent storage, event delivery and platform access | Versioned records, typed ports |
| Runtime | Supervisors, leases, scheduling and checkpoints | Leased task handles |
| Intelligence | Model capability negotiation, context and proposals | Typed generation and embedding service |
| Assignments | Durable plan, state machine, evidence and effect reconciliation | Command gateway |
| Engineering | Repository, docs, builds, tests and change staging | Pinned snapshot and governed adapters |
| Verification | Independent checks and acceptance verdict | Evidence records |
| Cross-cutting controls | Identity, authorization, sandbox, audit and resource gates | Re-evaluated effect authorization |

## Execution and ownership

1. Resolve immutable source, configuration and policy references. Validate and persist a plan before launch.
2. Reserve resources and issue a lease. Persist effect intent and audit an authorization decision before external execution.
3. Write outputs to bounded staging. Verify artifacts and atomically commit evidence and state with an outbox event.
4. Reconcile ambiguous external effects by effect key, then continue or block. Resume from the highest contiguous verified checkpoint.
5. Serve read-only progress through replayable event cursors. Treat reads from models and integrations as untrusted.

The composition root wires adapters at startup. Optional providers fail independently. The [dependency rules](specifications/0100-architecture/dependency-rules.md) and [storage contract](specifications/2500-storage/storage.md) define invariants shared across crates.
