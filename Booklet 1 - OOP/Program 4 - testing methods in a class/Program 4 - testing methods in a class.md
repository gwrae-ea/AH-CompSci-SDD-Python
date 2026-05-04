# Program 4 - Testing Methods in a Class

### Technical Explanation

This program demonstrates testing and calling methods on objects to verify they work correctly. Having defined methods in the previous program, this program shows how to call those methods with various inputs and verify their outputs. Testing methods is crucial to ensure objects behave as expected. The program demonstrates calling methods with different parameters, capturing return values, and verifying the results match expectations. This includes edge cases (boundary conditions) and normal use cases. Key technical skills include method invocation syntax, passing arguments to methods, interpreting return values, and systematic testing of object behavior.

---

## Analysis

### End User Requirements

1. The user wants to verify that methods work correctly before relying on them in production.
2. The user wants to test methods with various inputs to ensure they handle all cases.
3. The user wants clear evidence that methods are returning correct results.
4. The user wants to identify and fix any bugs in method implementations.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Call methods on test objects systematically.

FR2 Pass various parameter values to test methods under different conditions.

FR3 Capture and verify return values against expected results.

FR4 Test edge cases and boundary conditions.

#### Integration

The solution is required to:

FR5 Display test results clearly to show method behavior.

FR6 Compare actual results against expected values.

FR7 Report test pass/fail status for each test case.

#### Additional functional requirements

The solution is required to:

FR8 Test each method independently and in combination.

FR9 Include edge cases (zero, negative, maximum values, empty strings).

FR10 Display clear output showing all test cases and results.

FR11 Document what each test case is verifying.

---

## Design

### Test Structure

```
CREATE test object
FOR EACH test case
    CALL method with test parameters
    CAPTURE return value
    COMPARE against expected value
    DISPLAY pass or fail status
END FOR
```

---

## Implementation

[Program 4 - testing methods in a class.py](./Program%204%20%E2%80%93%20testing%20methods%20in%20a%20class.py)

### Notes

- Test with extreme values (very high/low numbers, empty strings, etc.)
- Test state changes (verify object properties change after method calls)
- Test multiple calls in sequence
- Compare actual vs expected values

---

## Test plan

| Test Case | Method | Input | Expected Output | Evidence |
|-----------|--------|-------|-----------------|----------|
| Normal case | get_full_name | Employee with name="John" "Smith" | "John Smith" | Before: None / After: "John Smith" |
| Normal case | calculate_monthly_salary | salary=$60000 | $5000.00 | Before: 0 / After: $5000.00 |
| Boundary case | apply_raise | raise=0% | Same salary | Before: Changed / After: Unchanged |
| Boundary case | apply_raise | raise=100% | Double salary | Before: Original / After: 2x original |
| State change | apply_raise | raise=10% | Salary increases by 10% | Before: $50000 / After: $55000 |

