# Agent roles and delegation

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Role manifests name capabilities, permissions, model requirements and budget. Coordinator, author and reviewer have distinct logical principals even if they share a model.

## Procedure

Place agents under an assignment scope with bounded mailboxes. Delegate only capabilities held by the parent and required for the task. A reviewer checks exact artifact digest and verifier identity.

## Verification and recovery

Agent messages are proposals. Unresolved conflict escalates to human review. Agents cannot self-approve grants or treat another agent's vote as execution evidence.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
