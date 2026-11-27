# Architecture overview

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Applications share a gateway; core services own assignment, policy, execution and verification state; adapters isolate platforms and providers.

## Procedure

Follow the immutable data flow from snapshot and plan to leases, outputs, verification, checkpoint and outbox. Runtime does not treat conversational history as durable job state.

## Verification and recovery

Validate that the smallest native profile starts without external services and advertises unavailable optional features explicitly.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
