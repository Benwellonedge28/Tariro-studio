# Tester role

**ZIP-AGENTS-ROLES-TESTER-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/tester.rs`

## Boundary and inputs

Run approved fixtures against an exact candidate, known adapter edition and authorized sandbox. Capture command or adapter invocation, inputs, actual outputs and result provenance under admitted time and storage budgets. Preserve synthetic fixture identity and distinguish blocked startup, cancelled, failed, passed and skipped outcomes.

## Behavior and failure handling

Bind evidence to checks, candidate, environment and actual receipts. A fabricated or unavailable result cannot satisfy verification. A retry uses the approved isolated fixture and records both attempts without overwriting earlier evidence. Disclose only scoped redacted output and communicate no production approval. See [testing](../../../../../specifications/1900-testing/testing.md).

## Acceptance

**ZIP-AGENTS-ROLES-TESTER-T01.** Mark a required check skipped and provide a second passing check. Verify the skipped check remains explicit and the mandatory gate stays blocked until a current verified result exists.
