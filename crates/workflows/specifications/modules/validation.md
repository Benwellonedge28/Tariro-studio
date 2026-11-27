# Workflow structural and policy validation

**ZIP-WORKFLOWS-VALIDATION-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/validation.rs`

Validate schema and identity, scoped node and output uniqueness, supported capability/effect combinations, complete typed bindings and declared dependencies, then cycle and checked expansion bounds. Reject unknown required fields and forward artifact references without a declared edge. Leaf adapters declare typed inputs and outputs, effect class, approval and resource requirements, and normalized shared-write keys. A registry entry supplies a capability description, never permission to invoke it. Unresolved effect or write capability prevents compilation. Revalidate current authority before execution regardless of compile results.

Use `workflows.max_expanded_steps` and `workflows.max_nesting_depth` from effective policy and any tighter definition or assignment ceilings. Reject invalid or absent effective limits and all arithmetic overflow. Check count and depth before constructing or allocating the expanded graph. A rejected graph cannot enqueue a task or create an execution effect.

**ZIP-WORKFLOWS-VALIDATION-T01.** With a bound below the projected expansion, reject before allocating executable nodes and enqueue zero children.
