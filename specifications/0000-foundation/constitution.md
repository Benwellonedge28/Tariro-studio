# Constitution enforcement

**Contract version** 1.0. Master design §71.

Implement the root constitutional rules through gateway, adapter and CI controls. Each enforcement record captures rule ID, enforcement boundary, deny code and test coverage. Configuration can tighten mandatory rules. Policy loading fails if version, integrity or required fields are invalid.

## Implementation and acceptance

Exercise startup with unsupported policy version, a missing sandbox capability and a configuration override of mandatory offline mode. All three must block affected operations.

[Binding rules](../../CONSTITUTION.md)
