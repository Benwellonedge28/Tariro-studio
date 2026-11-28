# Agent context assembly boundary

**ZIP-AGENTS-CONTEXT-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/context.rs`

## Boundary and inputs

Accept assignment, agent and task bindings, approved context sources, pinned revisions and a resolved byte or token envelope. Use only context assembly supplied by the authorized Intelligence integration. Return a bounded immutable reference or isolated per-attempt session whose audience, source hashes and policy revision can be verified.

## Behavior and failure handling

Authorize each fragment before reading or returning it. Scope mutable session state and cache keys by workspace, assignment, agent and applicable revisions. A shared model may reuse qualified immutable weights. Concurrent requests must keep their prompts, private state and output sessions isolated. Deny stale or unavailable required inputs and avoid transferring credentials. Check data disclosure at the model boundary independently from resource fit.

## Acceptance

**ZIP-AGENTS-CONTEXT-T01.** Run two roles concurrently against the same synthetic model with distinct private markers. Verify no crossover in context, cache lookup, model requests or output. Replay under revoked scope and confirm no private context is disclosed.
