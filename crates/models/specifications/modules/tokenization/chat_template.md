# Scoped chat template rendering

**ZIP-MODELS-TOKENIZATION-CHAT-TEMPLATE-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/tokenization/chat_template.rs`

## Required implementation behavior

Pin template and tokenizer, render approved roles with escaped untrusted content and account exact token overhead. Do not execute arbitrary template code.

## Acceptance

**ZIP-MODELS-TOKENIZATION-CHAT-TEMPLATE-T01.** Message data cannot become a privileged role delimiter.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
