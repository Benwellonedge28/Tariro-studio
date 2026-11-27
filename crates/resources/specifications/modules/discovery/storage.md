# Volume capacity and containment

**ZIP-RESOURCES-DISCOVERY-STORAGE-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/storage.rs`

## Required implementation behavior

Resolve workspace to an approved volume, measure available bytes and quota without trusting user path labels. File quotas and volume bytes are separate admission coordinates.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-STORAGE-T01.** Equal available bytes on another volume cannot satisfy this workspace's staging requirement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
