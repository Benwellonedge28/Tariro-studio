# Audit reader role

**ZIP-AGENTS-ROLES-AUDITOR-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/auditor.rs`

## Boundary and inputs

Read authorized redacted audit records, trusted checkpoints and effect receipts for one approved evidence scope. Produce a bounded report with exact base revision, checked sequence boundaries and provenance references. Require evidence of missing or skipped records to remain visible.

## Behavior and failure handling

Compare chain order, expected receipt linkage and record availability through the owning audit interface. Do not infer a clean outcome from an incomplete window. Report confirmed gap, integrity failure and unavailable evidence distinctly. The role cannot modify the chain or authorize any repair.

## Acceptance

**ZIP-AGENTS-ROLES-AUDITOR-T01.** Omit one record from a known required interval and replay a receipt with a wrong digest. Verify both gaps remain explicit and neither candidate is marked compliant.
