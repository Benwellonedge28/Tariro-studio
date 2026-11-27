# Hardware profiles

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

The initial reference machine has 16 GiB RAM and around 900 GB storage. The personal profile starts with a preference for sequential work and small-model inference. Use the minimal profile for deterministic workloads. Select local or separately authorized remote inference by measured capability and policy. Hardware labels describe candidate workloads, not admission thresholds.

## Procedure

Run doctor to probe capacity, instruction set, disk, sandbox and model backend support. Confirm host reserve and fit of weights plus context buffers before model load. A USB disk may house cold artifacts or models if permissions and storage latency pass checks.

## Verification and recovery

Treat hardware budgets as design targets. Record measured idle RSS, peak RAM/VRAM, temporary disk, model/context parameters, cancellation latency and any capability unavailable on the platform.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)

[Configuration profiles and effective limits](../../configurations/README.md).
