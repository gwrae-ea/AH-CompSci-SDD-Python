# Program 6 - Testing Encapsulation

### Technical Explanation

This program tests the encapsulation implementation from the previous program to verify that data protection is working correctly. It demonstrates attempts to access and modify properties both correctly (through setters) and incorrectly (direct property access), showing which operations are prevented by encapsulation. The program verifies that validation rules are enforced, that read-only properties cannot be changed, and that the object maintains data integrity. Testing encapsulation proves that the design protects against common programming errors and ensures constraints are maintained. Key technical skills include exception handling, testing constraint enforcement, validating that invariants are maintained, and demonstrating the defensive benefits of encapsulation.

---

## Analysis

### End User Requirements

1. The user wants to verify that invalid data cannot be stored in objects.
2. The user wants meaningful feedback when attempting invalid operations.
3. The user wants to see that encapsulation actually prevents data corruption.
4. The user wants to test both valid operations (should succeed) and invalid operations (should fail).

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Test all getter methods to verify they return correct values.

FR2 Test all setter methods with both valid and invalid inputs.

FR3 Verify that invalid inputs are rejected and raise appropriate exceptions.

FR4 Confirm that state changes only occur for valid operations.

#### Integration

The solution is required to:

FR5 Display clear test results showing pass/fail status.

FR6 Show both successful operations and prevented invalid operations.

FR7 Demonstrate that object state remains consistent.

#### Additional functional requirements

The solution is required to:

FR8 Test read-only properties to verify they cannot be modified.

FR9 Test boundary conditions (minimum/maximum values, empty strings).

FR10 Show that modifications through setters work but direct access does not.

FR11 Report total pass/fail count and coverage of test suite.

---

## Design

### Test Categories

1. **Getter Tests:** Verify getters return expected values
2. **Valid Setter Tests:** Verify valid data is accepted
3. **Invalid Setter Tests:** Verify invalid data is rejected
4. **State Change Tests:** Verify object state updates correctly
5. **Exception Tests:** Verify correct exceptions are raised
6. **Read-Only Tests:** Verify protected properties cannot be changed

---

## Implementation

[Program 6 - testing encapsulation.py](./Program%206%20%E2%80%93%20testing%20encapsulation.py)

### Notes

- Use try/except blocks to test for expected exceptions
- Verify that failed operations leave object state unchanged
- Test edge cases: zero, negative, empty, maximum length
- Demonstrate that encapsulation prevents errors

---

## Test plan

| Test Case | Operation | Expected | Evidence |
|-----------|-----------|----------|----------|
| Valid salary setter | set_salary(55000) | Updates to 55000 | Before: 50000 / After: 55000 |
| Invalid negative salary | set_salary(-100) | ValueError raised | Before: No error / After: ValueError |
| Invalid string salary | set_salary("abc") | ValueError raised | Before: No error / After: ValueError |
| Read-only ID property | set_employee_id(999) | AttributeError or ignored | Before: Can change / After: Cannot change |
| Name validation | set_first_name("") | ValueError for empty | Before: No error / After: ValueError |
| Name validation | set_first_name("A" * 100) | ValueError for too long | Before: No error / After: ValueError |

