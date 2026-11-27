# Installation and first boot

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Follow the release packaging workflow only once a signed release exists for the host. Match the target triple and minimum supported OS from the release manifest. Verify the package digest and release signature using the trusted verification key before launching.

## Procedure

Place the installed binary on PATH. Run zipporah init then zipporah doctor. Keep the data root and service socket private to the user. Resolve disk, permission and sandbox problems indicated by doctor before enabling agents. Inspect zipporah status and confirm default loopback or local IPC only.

## Verification and recovery

For upgrades back up the current metadata generation and artifacts; verify restore; stage replacement; run schema check; activate and run doctor. Retain the old binary and compatible backup until validation passes. Uninstall should preserve user data unless a separate explicit purge succeeds.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)
