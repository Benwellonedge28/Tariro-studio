# Orchestration engine boundary

**ZIP-ORCHESTRATION-LIB-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/lib.rs`

## Boundary and inputs

Declare the planned modules in the [Orchestration crate design](../../DESIGN.md) and forbid unsafe first-party code. Export the planning, coordinated execution observation and typed result interfaces specified by their owners. Keep role binding constructors, speculative plan data, current ownership checks and recovery helpers private.

## Behavior and failure handling

Use Foundation, Agents, Assignments, Scheduler and Verification as the approved first-party dependencies. Composition binds authorization and trusted runtime observations through those services or injected interfaces. No direct dependency on runtime, resources, storage or network is introduced here. Importing the crate or constructing a graph does not start work, read credentials or create a network connection. External effects use approved owning services.

## Acceptance

**ZIP-ORCHESTRATION-LIB-T01.** Compile a consumer with a deterministic planning fixture and fake composed ports. Verify construction produces zero effect calls. Verify private delegated authority and accepted outcome constructors remain unavailable to downstream callers.
