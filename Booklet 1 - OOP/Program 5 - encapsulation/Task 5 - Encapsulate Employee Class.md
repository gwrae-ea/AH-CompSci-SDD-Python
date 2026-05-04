# Task 5 - Encapsulate Employee Class

## Objective

Refactor the Employee class to use encapsulation by converting properties to private (prefixed with underscore) and providing getter/setter methods with validation. This task demonstrates data protection and constraint enforcement.

---

## Context

You will refactor the Employee class from previous tasks to implement proper encapsulation.

Your task is to:

1. Convert all properties to private (`_property_name`)
2. Create getter methods for reading properties
3. Create setter methods with validation
4. Demonstrate that invariants are maintained
5. Show error handling for invalid operations

---

## Requirements

### Private Properties (FR2, FR4)
Convert all Employee properties to private naming convention:
- `_employee_id`
- `_first_name`
- `_last_name`
- `_salary`
- `_department`
- `_position`
- `_hire_date`

### Getter Methods (FR1, FR8)
Create a getter for each property:
```python
def get_employee_id(self):
    """Return the employee ID."""
    return self._employee_id

def get_first_name(self):
    """Return the employee's first name."""
    return self._first_name
```

### Setter Methods with Validation (FR1, FR3, FR9)

#### `set_employee_id(value)` (FR3)
- Validate: must be positive integer

#### `set_first_name(value)` (FR3)
- Validate: non-empty string, max 50 characters

#### `set_last_name(value)` (FR3)
- Validate: non-empty string, max 50 characters

#### `set_salary(amount)` (FR3)
- Validate: non-negative number (>= 0)
- Cannot be set to invalid value
- Raise ValueError if invalid

#### `set_department(value)` (FR3)
- Validate: non-empty string, max 50 characters

#### `set_position(value)` (FR3)
- Validate: non-empty string, max 50 characters

#### `set_hire_date(date_obj)` (FR3)
- Validate: date must be before today
- Validate: date must be valid

### Read-Only Properties (FR6)
Some properties should be read-only (getter only, no setter):
- `_employee_id` (typically assigned at creation, not changed)
- `_hire_date` (typically assigned at creation, not changed later)

### Error Handling (FR5, FR9)
- Raise `ValueError` with descriptive message for invalid data
- Example: `raise ValueError("Salary cannot be negative")`

### Validation Method (FR9)
Consider creating a private helper method for validation:
```python
def _validate_salary(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Salary must be a number")
    if amount < 0:
        raise ValueError("Salary cannot be negative")
    return True
```

---

## Implementation Steps

1. **Convert constructor to use private properties:**
   ```python
   def __init__(self, employee_id, first_name, last_name, salary, 
                department, position, hire_date):
       self._employee_id = employee_id
       self._first_name = first_name
       # ... etc
   ```

2. **Add getter methods for all properties**

3. **Add setter methods with validation for mutable properties**

4. **Update existing methods to use getters/setters:**
   ```python
   def get_full_name(self):
       return f"{self.get_first_name()} {self.get_last_name()}"
   ```

5. **Create validation helper method if needed**

---

## Testing Your Encapsulation

```python
if __name__ == "__main__":
    from datetime import date
    
    emp = Employee(
        employee_id=101,
        first_name="Alice",
        last_name="Johnson",
        salary=50000,
        department="IT",
        position="Developer",
        hire_date=date(2019, 1, 15)
    )
    
    print("=== Testing Getters ===")
    print(f"ID: {emp.get_employee_id()}")
    print(f"Name: {emp.get_first_name()} {emp.get_last_name()}")
    print(f"Salary: ${emp.get_salary():.2f}")
    
    print("\n=== Testing Valid Setter ===")
    emp.set_salary(55000)
    print(f"New Salary: ${emp.get_salary():.2f}")
    
    print("\n=== Testing Invalid Setter ===")
    try:
        emp.set_salary(-1000)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"Correctly rejected: {e}")
    
    print(f"\nSalary after invalid attempt: ${emp.get_salary():.2f}")
    
    print("\n=== Testing Read-Only Property ===")
    try:
        emp.set_employee_id(999)
        print("ERROR: Employee ID was changed!")
    except AttributeError:
        print("Correctly protected: Employee ID cannot be changed")
```

Expected output:
```
=== Testing Getters ===
ID: 101
Name: Alice Johnson
Salary: $50000.00

=== Testing Valid Setter ===
New Salary: $55000.00

=== Testing Invalid Setter ===
Correctly rejected: Salary cannot be negative

Salary after invalid attempt: $55000.00

=== Testing Read-Only Property ===
Correctly protected: Employee ID cannot be changed
```

---

## Functional Requirements Covered

- **FR1:** Implement property access control using getters/setters
- **FR2:** Use naming conventions for private members (underscore prefix)
- **FR3:** Add validation logic to setters
- **FR4:** Maintain consistent access patterns
- **FR5:** Display error messages for invalid modifications
- **FR6:** Allow read-only properties
- **FR8:** Document public interface
- **FR9:** Raise exceptions for invalid operations
- **FR10:** Demonstrate difference between direct and encapsulated access

