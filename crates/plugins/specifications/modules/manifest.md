# Versioned plugin manifest

**ZIP-PLUGINS-MANIFEST-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/manifest.rs`

## Required implementation behavior

Declare required interface, entry, imports, data classes, limits and artifact digests. Reject unknown mandatory fields.

## Acceptance

**ZIP-PLUGINS-MANIFEST-T01.** Undeclared host import blocks activation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
