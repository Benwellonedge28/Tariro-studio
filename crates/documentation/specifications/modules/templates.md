# Versioned section templates

**ZIP-DOCUMENTATION-TEMPLATES-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/templates.rs`

## Required implementation behavior

Resolve template schema and role, retain immutable template ID and validate applicable sections. A template provides structure, never facts or authority.

## Acceptance

**ZIP-DOCUMENTATION-TEMPLATES-T01.** Unsupported template version is rejected before authoring.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
