# Repository worktrees and publication

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Pin repository identity and revision, compile applicable instructions, and use a dedicated worktree. Review every old and new path, mode and blob before publication.

## Procedure

Bind commit and PR operations to exact scope and immutable reviewed diff. Reconcile uncertain push or PR results against stable identity and exact ref/marker. Do not repeat unknown remote mutations automatically.

## Verification and recovery

Use separate authority for deletion or merge. Preserve branch history and report actual remote checks, including missing or failed CI.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
