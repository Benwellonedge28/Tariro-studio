# Wasm component containment

**ZIP-SANDBOX-BACKENDS-WASM-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/backends/wasm.rs`

## Boundary and inputs

Bind the exact module or component digest, declared interface edition, approved host imports and resolved execution envelope. Verify required memory and execution-meter support before instantiation. Grant only scoped host interfaces qualified for the profile. Host callbacks use their own authority and resource checks.

## Behavior and failure handling

Reject unsupported imports before running guest code. A metering or memory stop is a distinct bounded result. Host calls or external effects already invoked remain under original intent until authenticated settlement. Guest success and termination provide only the applicable execution observation, with independent evidence for external effects.

## Acceptance

**ZIP-SANDBOX-BACKENDS-WASM-T01.** Use one fixture requesting a disabled host import and one approved fixture exhausting its configured meter. Verify typed distinct results, no call through the denied import and no implicit host resource release.
