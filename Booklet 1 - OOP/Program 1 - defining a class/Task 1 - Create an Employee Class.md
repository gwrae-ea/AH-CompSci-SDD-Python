# Task 1 - Create an Employee Class

## Objective

Define a Python class called `Employee` that represents employee data with appropriate properties to store employee information. This task introduces the fundamental OOP concept of class definition and property declaration.

---

## Context

You have been given an empty Python file: `Task 1 - Create an Employee Class.py`

Your task is to create a complete class definition that models an employee with all relevant properties.

---

## Requirements

### Class Definition (FR1, FR6, FR8)
- Create a class named `Employee` (use PascalCase as per conventions)
- Include an `__init__` method that accepts parameters for each property
- Store each parameter as an instance property using `self.property_name`

### Properties (FR1, FR2, FR3)
Define the Employee class with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `employee_id` | int | Unique employee identifier |
| `first_name` | str | Employee's first name |
| `last_name` | str | Employee's last name |
| `salary` | float | Annual salary |
| `department` | str | Department name |
| `position` | str | Job position title |
| `hire_date` | date | Date employee was hired |

### Output Method (FR10)
- Implement a `__str__` method that returns a readable string representation
- Format should be: `Employee(id=X, name=FirstName LastName, position=Title, department=Dept, salary=$XXXX.XX, hire_date=YYYY-MM-DD)`
- Or create a `__repr__` method for developer-friendly output

### Validation (FR9)
Optional but recommended:
- Validate that `employee_id` is positive
- Validate that `salary` is non-negative
- Validate that `first_name` and `last_name` are non-empty strings

### Documentation (FR11)
- Add a docstring to the class explaining its purpose
- Add docstrings or comments to each property explaining its use
- Document the `__init__` method parameters

---

## Implementation Steps

1. **Create the file structure:**
   ```python
   from datetime import date
   
   class Employee:
       """Represents an employee with key employment information."""
       
       def __init__(self, employee_id, first_name, last_name, salary, 
                    department, position, hire_date):
           # Initialize properties...
   ```

2. **Initialize properties in `__init__`:**
   - Assign each parameter to a corresponding `self.property_name`
   - For example: `self.employee_id = employee_id`

3. **Implement `__str__` method:**
   ```python
   def __str__(self):
       return (f"Employee(id={self.employee_id}, name={self.first_name} {self.last_name}, "
               f"position={self.position}, department={self.department}, "
               f"salary=${self.salary:.2f}, hire_date={self.hire_date})")
   ```

4. **Optional: Add validation:**
   - In `__init__`, check properties before assigning
   - Raise exceptions for invalid data

5. **Add comment documentation:**
   - Explain each property near its assignment
   - Add docstring to class and methods

---

## Testing Your Solution

Create test code at the bottom of your file:

```python
if __name__ == "__main__":
    # Test 1: Create an Employee instance
    emp1 = Employee(
        employee_id=101,
        first_name="John",
        last_name="Smith",
        salary=50000.00,
        department="IT",
        position="Developer",
        hire_date=date(2020, 3, 15)
    )
    
    # Test 2: Print the employee
    print(emp1)
    
    # Test 3: Access individual properties
    print(f"Name: {emp1.first_name} {emp1.last_name}")
    print(f"Salary: ${emp1.salary:.2f}")
    
    # Test 4: Create a second instance (verify independence)
    emp2 = Employee(
        employee_id=102,
        first_name="Jane",
        last_name="Doe",
        salary=45000.00,
        department="HR",
        position="Manager",
        hire_date=date(2019, 7, 1)
    )
    print(emp2)
```

Expected output:
```
Employee(id=101, name=John Smith, position=Developer, department=IT, salary=$50000.00, hire_date=2020-03-15)
Name: John Smith
Salary: $50000.00
Employee(id=102, name=Jane Doe, position=Manager, department=HR, salary=$45000.00, hire_date=2019-07-01)
```

---

## Functional Requirements Covered

- **FR1:** Developer defined class to represent employee data with appropriate properties
- **FR2:** Appropriate property names that clearly describe the data
- **FR3:** Properties implemented as instance variables
- **FR6:** Class follows Python naming conventions
- **FR8:** `__init__` method to initialize instance attributes
- **FR9:** Optional property validation
- **FR10:** `__str__` method for human-readable output
- **FR11:** Clear documentation via docstrings and comments

