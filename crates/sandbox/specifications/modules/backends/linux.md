# Linux isolation capability

**ZIP-SANDBOX-BACKENDS-LINUX-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/backends/linux.rs`

## Required implementation behavior

Negotiate available filesystem, cgroup/process and network controls with qualified adapters. Bind root and limits before exec. Report restricted deployment gaps.

## Acceptance

**ZIP-SANDBOX-BACKENDS-LINUX-T01.** Containerized host lacking required enforcement declines launch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
