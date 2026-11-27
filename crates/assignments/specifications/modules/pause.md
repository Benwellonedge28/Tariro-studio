# Pause at a settled boundary

**ZIP-ASSIGNMENTS-PAUSE-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/pause.rs`

A pause records the pending Pause disposition and worker fence under CAS. Stop intake immediately, then ask the supervisor to drain or cancel running work. Retain any checkpoint committed before the fence. New work and worker checkpoint commits are denied after it. Pause doesn't rewind recorded intents or provider receipts.

Paused requires verified cleanup and reconciliation of all dispatched effects. Until then the assignment stays Recovering with its stop disposition. A later authorized cancellation or revoked grant updates that disposition according to [state](state.md). A Paused record does not carry an execution lease. Resume requires current scope, the approved plan and the recovery checks.

**ZIP-ASSIGNMENTS-PAUSE-T01.** Pause after a lost PR response. No new operation starts. Remain Recovering until existing provider state settles, then expose Paused and preserve the receipt.
