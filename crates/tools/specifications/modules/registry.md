# Qualified capability registry

**ZIP-TOOLS-REGISTRY-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/registry.rs`

## Boundary and inputs

Index immutable admitted descriptors by tool identity and supported version with approved manifest digest, qualified adapter and effective scope. Validate proposed registration against the authorized registry revision and enforce uniqueness. A same-version different manifest is a conflict.

## Behavior and failure handling

Resolve the exact declared and currently allowed version. Do not silently choose another version, tool name or adapter when resolution fails. Keep historic versions and retirement evidence scoped. Lookup supplies metadata only, and execution requires permission and current qualification again.

## Acceptance

**ZIP-TOOLS-REGISTRY-T01.** Register conflicting bytes under one tool version and verify no overwrite. Request an incompatible version with a compatible sibling enrolled and confirm there is no silent fallback.
