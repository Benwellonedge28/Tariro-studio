# Structured process adapter

**ZIP-TOOLS-ADAPTERS-PROCESS-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/adapters/process.rs`

## Required implementation behavior

Translate reviewed typed arguments into controlled command, scoped environment and rooted cwd. Use supervised containment and bounded exit status/output.

## Acceptance

**ZIP-TOOLS-ADAPTERS-PROCESS-T01.** Untrusted text does not change executable or create a shell pipeline.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
