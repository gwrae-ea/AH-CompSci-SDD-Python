# Task 4 - Test Employee Methods

## Objective

Write comprehensive tests for all Employee class methods to verify they work correctly with various inputs and edge cases. This task demonstrates systematic testing and validation of object-oriented code.

---

## Context

You have been given an empty Python file: `Task 4 - Test Employee Methods.py`

You will test the Employee class with methods from [Task 3](../Program%203%20-%20creating%20methods%20in%20a%20class/Task%203%20-%20Add%20Methods%20to%20Employee%20Class.md).

Your task is to create a comprehensive test suite.

---

## Requirements

### Test Organization (FR8, FR10, FR11)
- Organize tests logically by method
- Create a test suite with clear headers and descriptions
- Document what each test is verifying
- Display test results in a readable format

### Test Cases for Each Method (FR1, FR2, FR3)

#### `get_full_name()` Tests
- **Test 1:** Normal case with typical names
- **Test 2:** Names with special characters (apostrophe, hyphen)
- **Test 3:** Single-letter first/last names

#### `calculate_monthly_salary()` Tests
- **Test 1:** Normal salary ($60,000 → $5,000/month)
- **Test 2:** Low salary ($12,000 → $1,000/month)
- **Test 3:** High salary ($240,000 → $20,000/month)

#### `apply_raise()` Tests (FR2, FR4, FR9)
- **Test 1:** Normal raise (10% increase) - Verify state change
- **Test 2:** Zero percent raise (no change)
- **Test 3:** Maximum raise (100% - doubles salary)
- **Test 4:** Invalid negative raise (validation test)
- **Test 5:** Invalid raise > 100% (validation test)
- **Verify:** Salary property actually updates

#### `get_employment_info()` Tests
- **Test 1:** Verify all properties included in output
- **Test 2:** Verify formatting is readable
- **Test 3:** Verify special characters handled correctly

#### `years_employed()` Tests
- **Test 1:** Employee hired 1 year ago
- **Test 2:** Employee hired 5+ years ago
- **Test 3:** Recently hired (less than 1 year)

### Verification (FR3, FR6, FR7)
- Compare each actual result against expected value
- Display pass/fail for each test
- Show actual vs expected when test fails
- Track total pass/fail count

### Edge Cases (FR4, FR9)
- Test with minimum valid values
- Test with maximum valid values
- Test with invalid inputs (negative, zero, too large)
- Test with empty or unusual strings

---

## Implementation Steps

1. **Create test data:**
   ```python
   from datetime import date
   
   # Test employee
   test_emp = Employee(
       employee_id=100,
       first_name="Test",
       last_name="User",
       salary=50000,
       department="Testing",
       position="Tester",
       hire_date=date(2020, 1, 1)
   )
   ```

2. **Implement test function for each method:**
   ```python
   def test_get_full_name():
       print("\n=== Testing get_full_name() ===")
       result = test_emp.get_full_name()
       expected = "Test User"
       passed = result == expected
       print(f"Result: {result}")
       print(f"Expected: {expected}")
       print(f"Status: {'PASS' if passed else 'FAIL'}")
       return passed
   ```

3. **Create main test runner:**
   ```python
   if __name__ == "__main__":
       print("=" * 50)
       print("EMPLOYEE CLASS TEST SUITE")
       print("=" * 50)
       
       results = []
       results.append(test_get_full_name())
       results.append(test_calculate_monthly_salary())
       results.append(test_apply_raise())
       # ... more tests ...
       
       print(f"\n{'=' * 50}")
       print(f"TOTAL: {sum(results)}/{len(results)} tests passed")
       print(f"{'=' * 50}")
   ```

---

## Testing Output Format

```
==================================================
EMPLOYEE CLASS TEST SUITE
==================================================

=== Testing get_full_name() ===
Test 1: Normal case
  Result: Test User
  Expected: Test User
  Status: PASS

=== Testing calculate_monthly_salary() ===
Test 1: $60,000 annual
  Result: $5000.00
  Expected: $5000.00
  Status: PASS

=== Testing apply_raise() ===
Test 1: 10% raise
  Before: $50000.00
  After: $55000.00
  Expected increase: $5000.00
  Status: PASS

==================================================
TOTAL: 15/15 tests passed
==================================================
```

---

## Functional Requirements Covered

- **FR1:** Call methods on test objects systematically
- **FR2:** Pass various parameter values to methods
- **FR3:** Capture and verify return values
- **FR4:** Test edge cases and boundary conditions
- **FR5:** Display test results clearly
- **FR6:** Compare actual vs expected values
- **FR7:** Report pass/fail status for each test
- **FR8:** Test each method independently
- **FR9:** Include edge cases (zero, negative, maximum values)
- **FR10:** Display clear output showing all tests
- **FR11:** Document what each test verifies

