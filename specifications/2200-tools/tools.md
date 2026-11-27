# Governed tool execution

**Contract version** 1.0. Master design §71.

## Contract

A descriptor identifies capability, version, argument schema, limits, effect class, path and destination bindings. Validate requests before any process, file or network effect. Use structured argv and scoped filesystem handles.

## Execution and integration

Privileged effects go through the audit and approval gateway. Recover ambiguous operations by typed receipt; reject unavailable OS isolation. Cancellation must stop descendant processes.

## Verification

Run process-tree, output-limit, path-escape and malformed schema regressions using synthetic fixtures.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [tools crate design](../../crates/tools/DESIGN.md)
- [terminal crate design](../../crates/terminal/DESIGN.md)
- [filesystem crate design](../../crates/filesystem/DESIGN.md)
- [sandbox crate design](../../crates/sandbox/DESIGN.md)
