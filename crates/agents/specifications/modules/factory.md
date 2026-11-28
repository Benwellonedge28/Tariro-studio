# Validated agent construction

**ZIP-AGENTS-FACTORY-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/factory.rs`

## Boundary and inputs

Accept a verified artifact descriptor, requested scoped AgentId, owner authority and approved adapter observations. Verify exact manifest digest and supported mandatory fields before constructing the instance. Check model compatibility, capability intersection and finite mailbox envelope without loading a model, spawning a process or making a network request.

## Behavior and failure handling

Register only after all mandatory checks pass, using the original registration identity at the owning registry. Leave optional unavailable modes explicitly disabled under policy. A failed composition exposes no partial instance or authority. A lost registration reply must be resolved by registry identity before another creation. Admission and startup are separate authorized commands.

## Acceptance

**ZIP-AGENTS-FACTORY-T01.** Select an unsupported model and inject manifest digest mismatch. Neither path starts a worker or commits registration. Lose a valid registration acknowledgement and verify one instance under the original identity.
