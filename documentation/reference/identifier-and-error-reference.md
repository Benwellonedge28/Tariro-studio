# Identifiers and error conventions

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Use non-nil typed UUIDs for local entities, provider-specific immutable IDs for repositories, and tagged digests for immutable artifacts. UTC RFC 3339 timestamps are for interchange; measure live intervals with a monotonic clock.

## Procedure

An error carries code, stage, correlation ID, safe details and retryability. Standard codes include invalid_input, scope_denied, quota_exceeded, unsupported_capability, stale_revision and unknown_remote_outcome.

## Verification and recovery

An unknown external outcome requires reconciliation rather than immediate retry. Cancellation after durable commit reports committed result with an appropriate status.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
