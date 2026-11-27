# Authoring workflows

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Start with a strict versioned TOML definition. Each stage declares typed inputs and outputs, capability, dependencies, limits and effect class. Select deterministic templates for repeated tasks.

## Procedure

Validate before running, inspect the compiled plan and grant exact scope. Reuse idempotency keys during reconnect. Advance checkpoints after verified units; use explicit compensation adapters if permitted.

## Verification and recovery

A plan edit generates a new revision. Replay binds the previous definitions and evidence, and never repeats an unknown effect before reconciliation.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
