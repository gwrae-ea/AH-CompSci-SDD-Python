# Task 8 - Test Inheritance 1

## Objective

Write tests to verify that the Manager class correctly inherits from Employee and that all inheritance mechanisms work properly.

---

## Context

You will test the Manager class from [Task 7](../Program%207%20-%20inheritance/Task%207%20-%20Implement%20Inheritance.md).

Your task is to verify:
1. Manager can be created successfully
2. Manager inherits all Employee properties
3. Manager inherits all Employee methods
4. Manager-specific members work correctly
5. Method overrides work as intended

---

## Requirements

### Inheritance Verification Tests (FR1, FR2, FR3)

#### Test 1: Class Creation
```python
mgr = Manager(200, "Alice", "Johnson", 80000, "IT", "Manager", 
              date(2015, 6, 1), team_size=5, budget=500000)
assert mgr is not None
```

#### Test 2: isinstance Checks
```python
assert isinstance(mgr, Manager)
assert isinstance(mgr, Employee)
print(f"Manager is an instance of Manager: {isinstance(mgr, Manager)}")
print(f"Manager is an instance of Employee: {isinstance(mgr, Employee)}")
```

### Inherited Property Access Tests (FR8, FR2)

Test accessing parent properties through getters:
```python
# Test inherited properties
tests_passed = 0

# Test get_full_name (inherited method)
name = mgr.get_full_name()
if name == "Alice Johnson":
    print("PASS: get_full_name() inherited from Employee")
    tests_passed += 1
else:
    print(f"FAIL: get_full_name() returned '{name}'")

# Test get_salary (inherited method)
salary = mgr.get_salary()
if salary == 80000:
    print("PASS: get_salary() inherited from Employee")
    tests_passed += 1
else:
    print(f"FAIL: get_salary() returned {salary}")
```

### Inherited Method Tests (FR3, FR9)

Test calling parent class methods on child instances:
```python
# Test calculate_monthly_salary()
monthly = mgr.calculate_monthly_salary()
expected_monthly = 80000 / 12
if abs(monthly - expected_monthly) < 0.01:
    print(f"PASS: calculate_monthly_salary() = ${monthly:.2f}")
    tests_passed += 1
else:
    print(f"FAIL: calculate_monthly_salary() = {monthly}, expected {expected_monthly}")

# Test years_employed()
years = mgr.years_employed()
if years >= 8:  # Hired in 2015, so at least 8 years
    print(f"PASS: years_employed() = {years} years")
    tests_passed += 1
```

### Child-Specific Property Tests (FR6)

Test manager-specific properties:
```python
# Test Manager-specific properties
team_size = mgr.get_team_size()
if team_size == 5:
    print(f"PASS: get_team_size() = {team_size}")
    tests_passed += 1

budget = mgr.get_budget()
if budget == 500000:
    print(f"PASS: get_budget() = ${budget:,.2f}")
    tests_passed += 1
```

### Child-Specific Method Tests (FR6, FR9)

Test manager-specific methods:
```python
# Test budget_per_employee calculation
budget_per_emp = mgr.get_budget_per_employee()
expected = 500000 / 5
if abs(budget_per_emp - expected) < 0.01:
    print(f"PASS: get_budget_per_employee() = ${budget_per_emp:,.2f}")
    tests_passed += 1

# Test add_team_member
mgr.add_team_member()
if mgr.get_team_size() == 6:
    print(f"PASS: add_team_member() - Team size now {mgr.get_team_size()}")
    tests_passed += 1
```

### Method Override Tests (FR7)

Test if parent methods are correctly overridden:
```python
# Test get_info() override
info = mgr.get_info()
if "Managing" in info or "Budget" in info:
    print("PASS: get_info() override shows manager info")
    tests_passed += 1
else:
    print("FAIL: get_info() doesn't show manager-specific info")
```

### No Property Conflicts (FR4, FR11)

Verify parent and child properties don't conflict:
```python
# Verify no conflicts between Employee and Manager properties
emp_properties = ['_employee_id', '_first_name', '_salary', '_team_size']
# Confirm Manager can access all without errors
```

---

## Implementation Steps

1. **Create test function for inheritance verification:**
   ```python
   def test_inheritance_verification():
       print("\n=== Inheritance Verification ===")
       tests_passed = 0
       
       mgr = Manager(200, "Alice", "Johnson", 80000, "IT", "Manager",
                    date(2015, 6, 1), team_size=5, budget=500000)
       
       if isinstance(mgr, Manager) and isinstance(mgr, Employee):
           print("PASS: Manager is instance of both Manager and Employee")
           tests_passed += 1
       
       return tests_passed
   ```

2. **Create test functions for inherited methods**

3. **Create test functions for child-specific methods**

4. **Create test function for overrides**

5. **Create main runner:**
   ```python
   if __name__ == "__main__":
       total = 0
       total += test_inheritance_verification()
       total += test_inherited_properties()
       total += test_inherited_methods()
       total += test_child_properties()
       total += test_child_methods()
       total += test_method_overrides()
       
       print(f"\n{'='*50}")
       print(f"TOTAL: {total}/XX tests passed")
   ```

---

## Functional Requirements Covered

- **FR1-FR3:** Test inheritance, inherited properties, inherited methods
- **FR4:** Verify no property conflicts
- **FR5:** Display test results clearly
- **FR6:** Show distinction between inherited and child-specific
- **FR7:** Show method resolution
- **FR8-FR11:** Test property access, method calls, output, and inheritance verification

