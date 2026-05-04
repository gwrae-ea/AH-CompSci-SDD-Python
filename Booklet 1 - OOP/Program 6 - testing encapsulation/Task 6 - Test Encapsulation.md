# Task 6 - Test Encapsulation

## Objective

Write comprehensive tests for the encapsulated Employee class to verify that getters/setters work correctly and that validation prevents invalid data from being stored.

---

## Context

You will test the encapsulated Employee class from [Task 5](../Program%205%20-%20encapsulation/Task%205%20-%20Encapsulate%20Employee%20Class.md).

Your task is to create a comprehensive test suite covering:
- All getter methods
- All setter methods with valid inputs
- All setter methods with invalid inputs
- State preservation after failed operations
- Exception handling

---

## Requirements

### Getter Tests (FR1)
Test each getter to ensure it returns the correct value:
- `get_employee_id()`
- `get_first_name()`
- `get_last_name()`
- `get_salary()`
- `get_department()`
- `get_position()`
- `get_hire_date()`

### Valid Setter Tests (FR2, FR4)
Test each setter with valid inputs:

| Setter | Valid Input | Invalid Input |
|--------|-------------|---------------|
| `set_first_name()` | "John" | "", "A"*51, 123 |
| `set_last_name()` | "Smith" | "", "B"*51, None |
| `set_salary()` | 50000, 0, 1000000 | -100, "abc", None |
| `set_department()` | "IT" | "", "C"*51 |
| `set_position()` | "Developer" | "", "D"*51 |
| `set_hire_date()` | date(2019, 1, 1) | date.today(), "2019-01-01" |

### Invalid Setter Tests with Exception Handling (FR3, FR5)
```python
try:
    emp.set_salary(-100)
    print("FAIL: Should have raised ValueError")
except ValueError as e:
    print(f"PASS: ValueError raised - {e}")
```

Test cases:
- Negative salary
- Non-numeric salary
- Empty name strings
- Names exceeding max length
- Invalid date (in future)
- Invalid date (wrong type)

### State Preservation (FR4, FR6, FR7)
After each failed operation, verify the object state is unchanged:
```python
original_salary = emp.get_salary()
try:
    emp.set_salary(-100)
except ValueError:
    pass
assert emp.get_salary() == original_salary  # Unchanged
```

### Read-Only Property Tests (FR8)
Verify that read-only properties cannot be modified:
```python
try:
    emp.set_employee_id(999)
    print("FAIL: Employee ID was changed")
except AttributeError:
    print("PASS: Employee ID is read-only")
```

### Boundary Condition Tests (FR9)
Test edge cases:
- Salary = 0 (valid)
- Salary = very large number
- Name with 1 character
- Name with exactly 50 characters
- Name with 51 characters (should fail)

---

## Implementation Steps

1. **Create test employee:**
   ```python
   from datetime import date
   emp = Employee(101, "John", "Smith", 50000, "IT", "Developer", date(2019, 1, 1))
   ```

2. **Implement getter tests:**
   ```python
   def test_getters():
       print("\n=== Testing Getters ===")
       tests_passed = 0
       
       # Test get_first_name
       result = emp.get_first_name()
       if result == "John":
           print("PASS: get_first_name()")
           tests_passed += 1
       else:
           print(f"FAIL: get_first_name() - Expected 'John', got '{result}'")
       
       # ... test other getters
       return tests_passed
   ```

3. **Implement setter tests:**
   ```python
   def test_valid_setters():
       print("\n=== Testing Valid Setters ===")
       tests_passed = 0
       
       # Test valid salary
       emp.set_salary(55000)
       if emp.get_salary() == 55000:
           print("PASS: set_salary(55000)")
           tests_passed += 1
       else:
           print("FAIL: set_salary(55000)")
       
       # ... test other setters
   ```

4. **Implement invalid input tests:**
   ```python
   def test_invalid_setters():
       print("\n=== Testing Invalid Setters ===")
       tests_passed = 0
       
       # Test negative salary
       try:
           emp.set_salary(-100)
           print("FAIL: set_salary(-100) - Should have raised ValueError")
       except ValueError:
           print("PASS: set_salary(-100) - ValueError raised correctly")
           tests_passed += 1
       
       # ... test other invalid inputs
   ```

5. **Create main test runner:**
   ```python
   if __name__ == "__main__":
       total_passed = 0
       total_passed += test_getters()
       total_passed += test_valid_setters()
       total_passed += test_invalid_setters()
       total_passed += test_read_only()
       total_passed += test_state_preservation()
       print(f"\n{'='*50}")
       print(f"TOTAL: {total_passed}/XX tests passed")
   ```

---

## Testing Output Format

```
==================================================
EMPLOYEE ENCAPSULATION TEST SUITE
==================================================

=== Testing Getters ===
PASS: get_first_name()
PASS: get_salary()
PASS: get_hire_date()

=== Testing Valid Setters ===
PASS: set_salary(55000)
PASS: set_first_name("Jane")
PASS: set_department("Finance")

=== Testing Invalid Setters ===
PASS: set_salary(-100) - ValueError raised
PASS: set_first_name("") - ValueError raised
PASS: set_salary("abc") - ValueError raised

=== Testing Read-Only Properties ===
PASS: Employee ID is read-only

=== Testing State Preservation ===
PASS: Object state unchanged after failed salary update

==================================================
TOTAL: 20/20 tests passed
==================================================
```

---

## Functional Requirements Covered

- **FR1:** Test all getter methods
- **FR2:** Test all setter methods with valid inputs
- **FR3:** Verify invalid inputs are rejected
- **FR4:** Confirm valid operations change state correctly
- **FR5:** Display clear test results
- **FR6:** Show both success and prevention of invalid ops
- **FR7:** Demonstrate object state consistency
- **FR8:** Test read-only properties
- **FR9:** Test boundary conditions
- **FR10:** Demonstrate setters work, direct access doesn't
- **FR11:** Report total pass/fail count

