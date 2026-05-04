# Task 9 - Test Inheritance 2 (Polymorphism)

## Objective

Write tests that demonstrate polymorphism: creating a mixed collection of Employee and Manager objects, and calling methods that behave differently based on the actual object type.

---

## Context

You will test polymorphic behavior with Employee and Manager objects from previous tasks.

Your task is to:
1. Create a mixed collection of Employee and Manager objects
2. Call methods on each object and verify type-specific behavior
3. Show how polymorphism enables flexible code
4. Test method overrides in a realistic scenario

---

## Requirements

### Mixed Collection Tests (FR1, FR2)

Create a collection with both types:
```python
employees = []
employees.append(Employee(101, "Bob", "Smith", 50000, "IT", "Developer", date(2018, 1, 15)))
employees.append(Manager(201, "Alice", "Johnson", 80000, "IT", "Manager", date(2015, 6, 1), 
                         team_size=5, budget=500000))
employees.append(Employee(102, "Carlos", "Rodriguez", 55000, "HR", "Specialist", date(2019, 3, 20)))
```

### Polymorphic Method Calls (FR2, FR3, FR10)

Call the same method on all objects and show different results:
```python
print("=== Calling get_info() on All Employees ===")
for emp in employees:
    print(f"\n{emp.get_info()}")
    print("-" * 50)
```

Expected output should show:
- Employee objects show employee-specific info
- Manager objects show manager-specific info (team size, budget, etc.)

### Override Verification (FR3, FR4)

Test that overridden methods execute the correct version:
```python
def test_polymorphism():
    print("\n=== Testing Polymorphic Behavior ===")
    tests_passed = 0
    
    emp = Employee(101, "Bob", "Smith", 50000, "IT", "Developer", date(2018, 1, 15))
    mgr = Manager(201, "Alice", "Johnson", 80000, "IT", "Manager", date(2015, 6, 1),
                  team_size=5, budget=500000)
    
    # Both have apply_raise method
    emp.apply_raise(10)
    mgr.apply_raise(10)
    
    emp_salary_after = emp.get_salary()
    mgr_salary_after = mgr.get_salary()
    
    # If Manager overrides apply_raise, salaries might be different
    print(f"Employee salary after 10% raise: ${emp_salary_after:.2f}")
    print(f"Manager salary after 10% raise: ${mgr_salary_after:.2f}")
    
    return tests_passed
```

### Collection Processing (FR1, FR5, FR10)

Process mixed collection with polymorphism:
```python
def test_collection_processing():
    print("\n=== Processing Employee Collection ===")
    tests_passed = 0
    
    employees = [
        Employee(101, "Bob", "Smith", 50000, "IT", "Developer", date(2018, 1, 15)),
        Manager(201, "Alice", "Johnson", 80000, "IT", "Manager", date(2015, 6, 1), 
                team_size=5, budget=500000),
        Employee(102, "Carol", "White", 45000, "HR", "Specialist", date(2020, 6, 1))
    ]
    
    total_salary = 0
    manager_count = 0
    
    for emp in employees:
        total_salary += emp.get_salary()
        
        if isinstance(emp, Manager):
            manager_count += 1
            print(f"Manager: {emp.get_full_name()}, Team: {emp.get_team_size()}, Budget: ${emp.get_budget():,.2f}")
        else:
            print(f"Employee: {emp.get_full_name()}, Salary: ${emp.get_salary():,.2f}")
    
    print(f"\nTotal Employees: {len(employees)}")
    print(f"Managers: {manager_count}")
    print(f"Total Salary: ${total_salary:,.2f}")
    print(f"Average Salary: ${total_salary/len(employees):,.2f}")
    
    return tests_passed
```

### Type Checking Within Polymorphic Processing (FR3, FR6, FR9)

```python
def test_type_specific_processing():
    print("\n=== Type-Specific Processing ===")
    tests_passed = 0
    
    employees = [...]  # Mixed collection
    
    for emp in employees:
        # Polymorphic call - each type handles it
        info = emp.get_info()
        print(f"\n{type(emp).__name__}:")
        print(info)
        
        # Type-specific processing
        if isinstance(emp, Manager):
            # This code only runs for Managers
            budget_efficiency = emp.get_budget() / emp.get_salary()
            print(f"Budget-to-Salary Ratio: {budget_efficiency:.2f}")
        else:
            # This code only runs for Employees
            print(f"Individual Contributor: {emp.get_full_name()}")
    
    return tests_passed
```

### Method Override with super() Calls (FR8)

If your Manager class overrides a method and calls super():
```python
def test_super_calls():
    print("\n=== Testing super() Calls ===")
    
    mgr = Manager(201, "Alice", "Johnson", 80000, "IT", "Manager", date(2015, 6, 1),
                  team_size=5, budget=500000)
    
    # If Manager.apply_raise() calls super().apply_raise()
    mgr.apply_raise(10)
    
    # Verify both manager and employee logic executed
    if mgr.get_salary() > 80000:  # raise applied
        print(f"PASS: Salary increased to ${mgr.get_salary():.2f}")
    
    # And manager-specific logic (if any)
    print(f"Team still managing {mgr.get_team_size()} employees")
```

### Extensibility Demonstration (FR7, FR11)

```python
def test_extensibility():
    """Show how inheritance makes code extensible."""
    print("\n=== Extensibility Benefits ===")
    
    employees = [
        Employee(101, "Bob", "Smith", 50000, "IT", "Developer", date(2018, 1, 15)),
        Manager(201, "Alice", "Johnson", 80000, "IT", "Manager", date(2015, 6, 1), 
                team_size=5, budget=500000),
    ]
    # If we added Developer(extends Employee), Intern(extends Employee), etc.
    # The same code processes all types polymorphically
    # This demonstrates extensibility without modifying existing code
    
    for emp in employees:
        print(f"{type(emp).__name__}: {emp.get_full_name()} - ${emp.get_salary():,.2f}")
```

---

## Implementation Steps

1. **Create a main test file that:**
   - Imports Employee and Manager
   - Creates mixed collection
   - Tests polymorphic behavior
   - Shows type-specific processing

2. **Run collection processing:**
   ```python
   if __name__ == "__main__":
       test_polymorphism()
       test_collection_processing()
       test_type_specific_processing()
       test_super_calls()
       test_extensibility()
   ```

---

## Expected Output Format

```
=== Testing Polymorphic Behavior ===
Employee salary after 10% raise: $55000.00
Manager salary after 10% raise: $88000.00

=== Processing Employee Collection ===
Manager: Alice Johnson, Team: 5, Budget: $500,000.00
Employee: Bob Smith, Salary: $50000.00
Employee: Carol White, Salary: $45000.00

Total Employees: 3
Managers: 1
Total Salary: $175000.00
Average Salary: $58333.33

=== Type-Specific Processing ===

Manager:
Employee: Alice Johnson, Manager, IT, $88000.00
Managing 5 employees
Budget: $500,000.00
Budget-to-Salary Ratio: 5.68

Employee:
Employee: Bob Smith, Developer, IT, $55000.00
Individual Contributor: Bob Smith
```

---

## Functional Requirements Covered

- **FR1-FR4:** Mixed collections, polymorphic calls, override verification, realistic tests
- **FR5:** Display polymorphic behavior
- **FR6-FR7:** Show differences, demonstrate extensibility
- **FR8-FR11:** Test super calls, complex inherited behavior, clear output, flexible code

