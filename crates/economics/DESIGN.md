# Economics crate design

**Contract version** 1.0. Master design §54. Planned implementation.

## Responsibility and dependencies

Use versioned fixed-point prices with checked arithmetic, reserve before external request, settle actual recorded usage and release unused amount. Unknown outcome remains held until reconciled.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [resources](../resources/DESIGN.md)

- [Resources](../../specifications/0300-resources/resources.md)
- [Economics](../../specifications/3200-economics/economics.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `quote(work)`
- `reserve(estimate)`
- `settle(receipt)`
- `release(id)`

Record families: UsageEstimate, budget buckets, reservation, receipt and currency/minor-unit accounting. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `PriceQuote { schedule_revision, unit_kind, currency, rate_minor, expiry }`
- `BudgetReservation { id, scope, limit_minor, quantity }`
- `UsageReceipt { provider_request_id, units, price_revision }`

- `settle(reservation: ReservationId, receipt: UsageReceipt) -> Result<Settlement>`

## Failure, safety and resource limits

No money transfers. Budget amount zero disables spend. Undocumented or ambiguous rates require owner policy. Reconciliation cannot silently erase cost.

- `BudgetExceeded`
- `PriceUnknown`
- `ReceiptConflict`
- `SettlementPending`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/economics/src/
├── lib.rs
├── error.rs
├── budget.rs
├── usage.rs
├── pricing.rs
├── estimation.rs
├── accounting.rs
├── token_usage.rs
├── compute_usage.rs
├── storage_usage.rs
├── optimization.rs
├── provider_comparison.rs
├── spending_limits.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Concurrent requests cannot overspend. Test rounding and interrupted provider receipt.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`budget.rs`](specifications/modules/budget.md)
- [`usage.rs`](specifications/modules/usage.md)
- [`pricing.rs`](specifications/modules/pricing.md)
- [`estimation.rs`](specifications/modules/estimation.md)
- [`accounting.rs`](specifications/modules/accounting.md)
- [`token_usage.rs`](specifications/modules/token_usage.md)
- [`compute_usage.rs`](specifications/modules/compute_usage.md)
- [`storage_usage.rs`](specifications/modules/storage_usage.md)
- [`optimization.rs`](specifications/modules/optimization.md)
- [`provider_comparison.rs`](specifications/modules/provider_comparison.md)
- [`spending_limits.rs`](specifications/modules/spending_limits.md)
- [`reporting.rs`](specifications/modules/reporting.md)
