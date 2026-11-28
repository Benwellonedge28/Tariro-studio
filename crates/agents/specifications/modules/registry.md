# Agent role and instance registry

**ZIP-AGENTS-REGISTRY-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/registry.rs`

## Boundary and inputs

Index immutable registered agent identity, scoped membership, reviewed manifest digest and version, current principal epoch and retirement marker. Use the owning journal's expected revision for registration, retirement and replay. Reject conflicting descriptors for an existing key and require verified current membership before returning privileged views.

## Behavior and failure handling

Repeat registration with an identical authorized digest and return the original binding. A changed descriptor requires an explicitly approved new identity or version under the owning policy. Keep retired IDs non-reusable and retain historical receipt references. Display-name reuse cannot revive prior permissions. Registry lookup is observation and supplies no live effect grant.

## Acceptance

**ZIP-AGENTS-REGISTRY-T01.** Retire one agent, register another with the same display name and attempt original activation. Verify no revival, no private historical evidence crosses the new scope and a replay returns only an authorized historical result.
