# Structured process adapter

**ZIP-TOOLS-ADAPTERS-PROCESS-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/adapters/process.rs`

## Boundary and inputs

Translate only normalized arguments supplied by the approved tool descriptor into a typed executable, scoped working directory, bounded input/output and explicit environment. Bind command review, live lease, and Sandbox controls through application composition. No direct Tools-to-Terminal dependency is introduced.

## Behavior and failure handling

Submit the exact request through the supervised process boundary and record actual exit, stream completeness, teardown and external effects separately. Reject arbitrary command text and unavailable isolation. Do not interpret output as follow-on authority or declare success from an unverified exit.

## Acceptance

**ZIP-TOOLS-ADAPTERS-PROCESS-T01.** Send inert punctuation to a controlled synthetic argument recorder. Verify one expected executable and exact argument boundaries. Supply an unsupported working-directory proof and verify no process begins.
