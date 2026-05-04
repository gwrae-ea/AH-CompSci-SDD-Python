# Program 9 - Testing Inheritance 2

### Technical Explanation

This program continues testing inheritance but focuses on more advanced scenarios: polymorphism (treating different types uniformly), method overrides, and complex inheritance scenarios. The program demonstrates calling methods on a collection of mixed parent and child objects, handling polymorphic calls correctly, and verifying that the most specific implementation executes. It also tests method chaining (child calling parent via `super()`), inheritance-based processing, and shows how inheritance enables flexible, extensible code. This program validates not just that inheritance works, but that it enables the design patterns and flexibility that make OOP powerful.

---

## Analysis

### End User Requirements

1. The user wants to mix parent and child objects in collections and process them uniformly.
2. The user wants method overrides to execute the appropriate version based on object type.
3. The user wants to verify polymorphism works correctly.
4. The user wants to confirm that inheritance enables extensible design.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Store parent and child objects in the same collection.

FR2 Call methods on mixed collections correctly.

FR3 Verify polymorphic behavior (correct method version executes).

FR4 Test method overrides in realistic scenarios.

#### Integration

The solution is required to:

FR5 Display output showing polymorphic behavior.

FR6 Show how parent and child types behave differently.

FR7 Demonstrate extensibility benefits of inheritance.

#### Additional functional requirements

The solution is required to:

FR8 Test super() calls within methods.

FR9 Test complex method behavior with inherited state.

FR10 Display clear output showing polymorphic results.

FR11 Verify that inheritance enables flexible code patterns.

---

## Design

### Polymorphism Pattern

```
DECLARE employees ARRAY
ADD Employee(...)
ADD Manager(...)
ADD Developer(...)

FOR EACH emp IN employees
    CALL emp.get_info()    // Correct version executes
END FOR
```

---

## Implementation

[Program 9 - testing inheritance 2.py](./Program%209%20%E2%80%93testing%20inheritance%202.py)

### Notes

- Collections can hold parent and child objects
- Methods called on collection items use correct type-specific version
- Demonstrates true polymorphism
- Shows benefits of inheritance for extensible code

---

## Test plan

| Test Case | Operation | Expected | Evidence |
|-----------|-----------|----------|----------|
| Mixed collection | Add Employee and Manager to list | Both types stored | Before: TypeError / After: Both stored |
| Polymorphic call | Call method on mixed collection | Correct version executes | Before: Wrong method / After: Correct method |
| Override execution | Call overridden method on each type | Each executes its version | Before: All same / After: Type-specific |
| Super call test | Method calls super() | Parent version also executes | Before: Skipped / After: Called |
| Type-specific behavior | Different types show different output | Output reflects type | Before: Identical / After: Different |

