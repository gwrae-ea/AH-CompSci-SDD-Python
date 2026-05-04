# Program 8 - Testing Inheritance 1

### Technical Explanation

This program tests basic inheritance functionality to verify that child classes correctly inherit properties and methods from their parent class. The program creates instances of both parent and child classes and demonstrates that child objects have access to all parent functionality. It shows method resolution—when a method is called on a child object, the appropriate version (parent or child) executes. Testing inheritance is crucial to ensure the class hierarchy is correctly structured and that code reuse is functioning as expected. Key technical skills include verifying inheritance relationships, testing method resolution order, confirming property inheritance, and validating that overrides work correctly.

---

## Analysis

### End User Requirements

1. The user wants to verify that inheritance is correctly implemented.
2. The user wants to see which methods/properties are inherited vs added.
3. The user wants to confirm that child objects work as expected.
4. The user wants to validate that method overrides function correctly.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Test that child class instances exist and can be created.

FR2 Test that child instances access inherited properties.

FR3 Test that child instances call inherited methods correctly.

FR4 Verify property inheritance doesn't cause conflicts.

#### Integration

The solution is required to:

FR5 Display test results clearly showing what works.

FR6 Show distinction between inherited and child-specific members.

FR7 Demonstrate method resolution (which version executes).

#### Additional functional requirements

The solution is required to:

FR8 Test inherited property access patterns.

FR9 Test inherited method calls.

FR10 Display clear output showing inheritance hierarchy.

FR11 Verify no property conflicts between parent and child.

---

## Design

### Test Categories

1. **Inheritance Verification:** Confirm Manager inherits from Employee
2. **Inherited Properties:** Access parent properties on child
3. **Inherited Methods:** Call parent methods on child
4. **Child Properties:** Verify child-specific properties work
5. **Child Methods:** Verify child-specific methods work
6. **Method Resolution:** Confirm correct version runs

---

## Implementation

[Program 8 - testing inheritance 1.py](./Program%208%20%E2%80%93testing%20inheritance%201.py)

### Notes

- Verify `isinstance(mgr, Manager)` and `isinstance(mgr, Employee)`
- Test that parent methods work on child objects
- Show that child has both parent and child methods
- Demonstrate method overrides

---

## Test plan

| Test Case | Operation | Expected | Evidence |
|-----------|-----------|----------|----------|
| Child instance creation | Create Manager object | Object created successfully | Before: Error / After: Object exists |
| Inherited property access | Call get_full_name() on Manager | Returns correct name | Before: Error / After: Name returned |
| Inherited method call | Call calculate_monthly_salary() on Manager | Returns correct value | Before: Error / After: Value calculated |
| Child property access | Access team_size on Manager | Returns correct team size | Before: Error / After: Team size |
| isinstance check | isinstance(mgr, Employee) | True | Before: False / After: True |
| Method override check | Call overridden method | Child version executes | Before: Parent version / After: Child version |

