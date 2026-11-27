# Optional container backend

**ZIP-SANDBOX-BACKENDS-CONTAINER-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/backends/container.rs`

## Required implementation behavior

Verify runtime, image digest, mounts, networking and resource controls. Do not pass privileged host or secret mounts implicitly.

## Acceptance

**ZIP-SANDBOX-BACKENDS-CONTAINER-T01.** Unexpected mutable tag and unauthorized mount cause validation failure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
