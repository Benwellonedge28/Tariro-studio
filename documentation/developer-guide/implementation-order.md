# Developer implementation order

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Begin with foundation types, limits, structured errors and configuration, then embedded storage, events, runtime and resource admission. Wire all services through typed interfaces at composition root.

## Procedure

Implement each crate design against its numbered spec, add deterministic contract fixtures, and preserve dependency edges. Introduce optional integrations after the local path and failure cases pass. Evidence IDs map acceptance back to the requirements table.

## Verification and recovery

Each shipped feature must support failure classification, cancellation or reconcile behavior, and a clear compatibility declaration.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
