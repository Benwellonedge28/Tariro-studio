# Durable reservation reconciliation

**ZIP-ECONOMICS-ACCOUNTING-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/accounting.rs`

## Required implementation behavior

Reserve, record actual charge or unknown state, and release only proven unused capacity. Bind idempotency to exact provider effect and receipt.

## Acceptance

**ZIP-ECONOMICS-ACCOUNTING-T01.** Duplicate receipt cannot charge twice; missing receipt does not erase reservation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
