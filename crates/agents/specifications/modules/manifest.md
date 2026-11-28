# Versioned role manifest

**ZIP-AGENTS-MANIFEST-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/manifest.rs`

## Boundary and inputs

Define an immutable versioned AgentManifest describing declared role, typed capability editions, model requirements, data scope and resource preferences or caps. Bind workspace and assignment through the review envelope. Validate required fields, reject duplicate or unknown mandatory data and compare compatible type and unit declarations before producing a reviewed descriptor.

## Behavior and failure handling

Canonicalize stable fields and ordered sets under the declared codec before computing the Foundation-tagged digest. Keep raw credentials and live capabilities outside the manifest. The registered digest must equal the reviewed digest at activation and dispatch. An updated manifest needs an independently reviewed binding. An unqualified codec or unsupported mandatory edition blocks activation.

## Acceptance

**ZIP-AGENTS-MANIFEST-T01.** Reorder unordered fields and compare canonical digests. Change a model constraint or role and verify old approval is rejected. Submit unknown mandatory data and confirm no instance registers.
