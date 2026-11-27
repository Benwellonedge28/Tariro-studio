# Local administrator operations

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Configure workspace data root, user identities, default offline policy, resource profile, backups and audit retention. Start service under a least-privilege user. Remote access and telemetry need separate policy entries.

## Procedure

Verify private directory permissions, credential keyring access and current schema. Test backup restore monthly in a separate root and verify object hashes. Check daemon listener and enforce supported isolation before enabling untrusted tasks.

## Verification and recovery

On incident stop writes, revoke the scoped grant and collect redacted audit evidence. Restore service only after verifying integrity and reconciling pending effects.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
