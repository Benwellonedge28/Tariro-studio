# Agent instance identity

**ZIP-AGENTS-AGENT-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/agent.rs`

## Boundary and inputs

An agent instance binds one verified AgentId, principal epoch, workspace, assignment and reviewed manifest digest. Hold its approved role separately from the selected model route and adapter edition. Expose immutable identity and scoped lifecycle views. Only [factory](factory.md) may construct a registered instance through [registry](registry.md).

## Behavior and failure handling

Use the verified binding for every context request and task submission. An instance cannot exchange roles or widen capabilities by changing models. A changed manifest or identity requires a new authorized registry binding. Private state, mailbox and active attempt are scoped to the instance. Runtime owns execution and cleanup. Keep raw grant material and credentials outside instances.

## Acceptance

**ZIP-AGENTS-AGENT-T01.** Bind two agents to the same model and perform equivalent dispatch requests. Verify different principals and private state views and no borrowing of the other agent's role, mailbox or result rights.
