# Terminal result DTO

**ZIP-ASSIGNMENTS-RESULT-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/result.rs`

## Required implementation behavior

Represent Completed(receipts), Failed(typed cause), Cancelled(cleanup status) or Blocked(reason). Attach durable revision and redacted evidence IDs. No optional success synthesized from missing fields.

## Acceptance

**ZIP-ASSIGNMENTS-RESULT-T01.** Deserialize unknown mandatory outcome and fail; committed effect remains visible on cancellation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
