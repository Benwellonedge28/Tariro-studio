# Reservation lifecycle receipts

**ZIP-RESOURCES-ALLOCATION-RESERVATION-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/allocation/reservation.rs`

## Required implementation behavior

Bind reservation to assignment, attempt and exact pool coordinates. Store admitted vector and state Reserved/Active/Draining/Recovering/Released. Release needs verified cleanup and compatible epoch.

## Acceptance

**ZIP-RESOURCES-ALLOCATION-RESERVATION-T01.** Double release and cleanup from a different attempt return typed failures and preserve totals.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
