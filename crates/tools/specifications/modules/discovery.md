# Bounded discovery of available tools

**ZIP-TOOLS-DISCOVERY-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/discovery.rs`

## Boundary and inputs

Read only enrolled local registries and remote sources specifically authorized for discovery. Require finite page, byte, item and time budgets. Scope cursors to registry identity, version, actor and pinned negotiation. Distinguish installed, unsupported and unverified descriptors.

## Behavior and failure handling

Keep discovered metadata untrusted until qualification against reviewed manifest and policy. No discovery outcome grants a capability or causes execution. A missing cursor, incompatible version or unavailable mandatory egress produces explicit partial or unavailable state. Offline mode makes no remote discovery calls.

## Acceptance

**ZIP-TOOLS-DISCOVERY-T01.** Run offline with a synthetic remote registry present and observe zero external requests. Supply a continuation for another registry and verify denial without private listing disclosure.
