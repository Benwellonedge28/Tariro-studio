# Foundation dependency contract

**Maturity:** D4 candidate.

Foundation has no first-party dependency. The allowed external dependency roles are UUID representation/parser and qualified UTC conversion at a serialization adapter. Standard-library primitives implement owned values and process-local synchronization. Crypto hashing belongs to a consuming adapter; the digest module represents and encodes validated bytes only.

No terminal, network, storage, logger, runtime, GPU, provider SDK, global configuration, or OS credential API may enter a Foundation dependency signature. No boundary may be widened to obtain randomness from a hidden singleton. Inject an approved source into identifier generation.

Review actual Cargo metadata, feature resolution and dependency qualification before approving implementation. Offline fixture builds cannot fetch provider configuration or require credentials. See [dependency graph](../../../DEPENDENCY_GRAPH.md) and [workspace policy](../../../DEPENDENCIES.md).
