# Model registry and artifact lifecycle

**Contract version** 1.0. Master design §71.

## Contract

Manifest v1 records name, revision, format, tokenizer and weights digests, provenance URL/source, license, declared capabilities and minimum hardware. States are Staged, Downloading, Verifying, Ready, Quarantined or Evicted.

## Execution and integration

Resumable fragments carry byte length and source validator. On source change restart into a new temp file. Promote only after length and SHA-256 verification. Keep last-use metadata in local storage and never evict an active pin.

## Verification

Interrupt download after one chunk, change source version, and show that no corrupt weight becomes Ready.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [models crate design](../../crates/models/DESIGN.md)
- [providers crate design](../../crates/providers/DESIGN.md)
