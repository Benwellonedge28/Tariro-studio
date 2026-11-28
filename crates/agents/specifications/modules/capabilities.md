# Agent capability intersection

**ZIP-AGENTS-CAPABILITIES-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/capabilities.rs`

## Boundary and inputs

Describe declared capabilities as versioned action and scope requirements from the approved manifest. Intersect them with the currently authorized grant, exact task scope and qualified adapter support. Resolve mandatory capabilities before dispatch and evaluate them again immediately before the effect. Treat absence, unsupported edition and denied scope as distinct outcomes.

## Behavior and failure handling

Use declared compatibility rules when matching versions. Agent or model output can request a capability by name but cannot add it, widen its scope or choose an unauthorized fallback. Route qualified read-only observations under their own permissions. Preserve stable denial reasons and current policy provenance without revealing protected registry contents.

## Acceptance

**ZIP-AGENTS-CAPABILITIES-T01.** Request repository publishing from a read-only agent. Verify no publishing adapter is selected. Then remove the required adapter edition for a read operation and distinguish unsupported compatibility from policy denial without dispatch.
