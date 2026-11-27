# Pure condition evaluation

**ZIP-WORKFLOWS-CONDITION-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/condition.rs`

Parse the restricted guard language into a typed AST. Operands are named immutable input or predecessor output bindings, booleans, UTF-8 strings and signed 64-bit integers. Support equality and inequality within one type, integer order comparisons, parentheses, logical negation, conjunction and disjunction. Operator precedence is parentheses, comparisons, negation over Boolean expressions, conjunction then disjunction. Reject chained comparisons, implicit coercions, unknown names and functions. Require a Boolean result. Values from source text, events or artifacts never become executable expressions.

Read references from the persisted binding set. Resolve and validate all referenced fields in canonical name order before evaluation; an unresolved reference is MissingInput even when a later Boolean branch could short-circuit. Evaluate the validated Boolean expression left-to-right with Boolean short circuit and bounded steps and AST depth under the effective budget. String equality compares exact UTF-8 bytes. No I/O, clock, mutable global state, provider calls or random decisions are allowed.

**ZIP-WORKFLOWS-CONDITION-T01.** A missing operand in a guard remains an error, a mixed integer/string comparison is invalid, and repeated evaluation over the same inputs yields the same decision.
