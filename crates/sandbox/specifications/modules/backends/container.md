# Optional container backend

**ZIP-SANDBOX-BACKENDS-CONTAINER-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/backends/container.rs`

## Boundary and inputs

Require an approved local container adapter, immutable image digest, trusted provider and exact runtime configuration. Inspect requested mounts, network mode, device visibility, process limits and installed resource controls before allowing application code. Stage only scoped objects, with no inherited host credentials or dynamic image resolution.

## Behavior and failure handling

Bind an opaque restart-addressable containment locator. Treat missing runtime control, extra mount or image digest mismatch as setup failure while execution remains blocked. Adapter verification covers descendants and mount teardown. Treat ambiguous container creation as an outstanding obligation requiring trusted inspection.

## Acceptance

**ZIP-SANDBOX-BACKENDS-CONTAINER-T01.** Offer a mutable image tag, an unauthorized synthetic mount and an unavailable resource control. Each must fail before the fixture body starts. Run the approved image and verify removal only after whole-container teardown proof.
