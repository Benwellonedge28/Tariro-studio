# Native inference

**Contract version** 1.0. Master design §71.

## Contract

Probe format, context-length, device and memory capabilities without loading weights. Load only a verified manifest+tokenizer pair. Attach measured peak RAM/VRAM to the reservation and return a handle pinned to model digest, adapter version and device.

## Execution and integration

For the first release use a compatible interchangeable inference engine behind the contract. Implement optional embedded inference later. A failed quantization or device probe returns an unsupported result and does not enable a remote route.

## Verification

Test CPU-only, wrong format, model too large, request cancellation and reloading after cleanup.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [inference crate design](../../crates/inference/DESIGN.md)
- [resources crate design](../../crates/resources/DESIGN.md)
