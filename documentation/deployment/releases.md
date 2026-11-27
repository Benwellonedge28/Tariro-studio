# Release and deployment procedure

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Generate a manifest of signed artifacts, SHA-256 digests, target ABI, toolchain, SBOM and required evidence. Stage deployment without changing the running instance.

## Procedure

Verify compatibility and health in staging, obtain target-specific production approval, then activate through the selected native or approved optional adapter. Stop or roll back on failed health conditions.

## Verification and recovery

Record previous and current artifact IDs, deployment receipts and rollback evidence. A passing build does not grant release authority.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
