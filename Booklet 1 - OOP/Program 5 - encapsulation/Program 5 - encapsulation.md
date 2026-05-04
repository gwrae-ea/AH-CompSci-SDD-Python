# Program 5 - Encapsulation

### Technical Explanation

This program demonstrates the principle of encapsulation, a core OOP concept that involves hiding internal object details and controlling access to properties. Rather than allowing direct modification of properties from outside the object, encapsulation uses methods to manage data. This program shows how to use private properties (by convention, prefixed with underscore) and public getter/setter methods to control how data is accessed and modified. Encapsulation ensures validity constraints (e.g., salary cannot be negative), prevents accidental misuse, and allows internal implementation changes without affecting external code. Key technical skills include naming conventions for private vs public members, property validation, data hiding, and the getter/setter pattern.

---

## Analysis

### End User Requirements

1. The user wants invalid data to be prevented from being stored in objects.
2. The user wants confidence that properties will not be corrupted by external code.
3. The user wants to see meaningful error messages when attempting invalid operations.
4. The user wants internal implementation details to be hidden from external view.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Implement property access control using getter and setter methods.

FR2 Use naming conventions to indicate private vs public members (underscore prefix).

FR3 Add validation logic to setters to prevent invalid data.

FR4 Maintain consistent access patterns throughout the class.

#### Integration

The solution is required to:

FR5 Display error messages for invalid property modification attempts.

FR6 Allow read-only properties where modification is not permitted.

FR7 Demonstrate that encapsulation prevents data corruption.

#### Additional functional requirements

The solution is required to:

FR8 Document public interface (getters/setters) clearly.

FR9 Raise exceptions or return error codes for invalid operations.

FR10 Show the difference between direct property access and encapsulated access.

---

## Design

### Encapsulation Pattern

```
CLASS Employee
    PRIVATE: _employee_id, _first_name, _salary, etc.
    
    PUBLIC METHOD get_salary()
        RETURN _salary
    END METHOD
    
    PUBLIC METHOD set_salary(amount)
        IF amount >= 0 THEN
            _salary = amount
        ELSE
            RAISE error
        END IF
    END METHOD
END CLASS
```

---

## Implementation

[Program 5 - encapsulation.py](./Program%205%20%E2%80%93%20encapsulation.py)

### Notes

- Properties prefixed with underscore are conventionally private
- Access through getter/setter methods provides control
- Setters validate data before assignment
- Makes code more robust and maintainable

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Valid setter | set_salary(50000) | Salary updated to 50000 | Before: Old value / After: 50000 |
| Invalid setter | set_salary(-100) | Error raised, salary unchanged | Before: Unchanged / After: Error raised |
| Getter access | get_salary() | Returns current salary | Before: Error / After: Salary value |
| Constraint enforcement | set_salary(0) | Accepted (0 is valid) or rejected | Before: Undefined / After: Clear behavior |
| Data isolation | Modify _property directly bypasses validation | Demonstrates need for encapsulation | Before: No validation bypass / After: Shows vulnerability |

