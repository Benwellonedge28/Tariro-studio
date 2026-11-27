# Security operator controls

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Use least privilege, local keyring and intersected RBAC, ABAC and capability grants. Retain redacted audit evidence for every privileged effect.

## Procedure

Start in offline mode and grant explicit network destinations only when needed. Use emergency stop to prevent new effects and reconcile prior in-flight writes. Test secret redaction with synthetic canaries.

## Verification and recovery

Never turn off sandbox isolation to recover a failing job. Rotate credentials in their owner service if exposure is suspected and record the incident disposition.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
