# Static iteration expansion

**ZIP-WORKFLOWS-LOOPING-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/looping.rs`

Edition 1 supports static repeats. The positive finite repeat count is part of the reviewed immutable definition, with an implicit count of one where a repeat is absent. A runtime value, live cursor or provider response cannot create iterations. A scope carries exact normalized ID components. Expanded leaves identify each repeated ancestor and leaf with a zero-based ordinal for every repetition. Use the sequence of scoped components and ordinals rather than a display string as the canonical node ID.

Compute per-scope effective count as the checked sum of child counts times the scope repeat, or the repeat count for a leaf. Start root depth at one for the first declared step. Check nested depth as scopes are entered and count before allocating expanded nodes. The first repeated instance inherits the declared entry prerequisites. Later instances also wait for terminal successful exits of the prior instance. Require typed entry and exit bindings that resolve to stable nodes under expansion. Missing exits or references across ambiguous repeated scopes fail validation.

**ZIP-WORKFLOWS-LOOPING-T01.** Expand a two-iteration group with three leaves to six stable leaves. A cap of five or arithmetic overflow rejects the entire executable graph without scheduling.
