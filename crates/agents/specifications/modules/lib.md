# Agent runtime boundary

**ZIP-AGENTS-LIB-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/lib.rs`

## Boundary and inputs

Declare modules from the [Agents crate design](../../DESIGN.md) and forbid unsafe first-party code. Export typed manifest and identity views, agent status, errors and the authorized lifecycle and dispatch interface. Keep mutable registry, mailbox and state transitions, provisional outputs and private authority constructors inside the crate.

## Behavior and failure handling

Use Foundation, Governance, Intelligence and Runtime as the only first-party dependencies. Composition supplies other identity, persistence and verification evidence through bounded typed interfaces. Import and object construction do not enable work, enumerate models, read credentials or open network connections. Effect controls require explicitly assembled, validated adapters.

## Acceptance

**ZIP-AGENTS-LIB-T01.** Compile a synthetic consumer inspecting a manifest and state view through public exports. Verify no adapter calls occur and the consumer cannot construct an approved grant or mutate the mailbox directly.
