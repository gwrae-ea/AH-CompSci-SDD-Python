# Task 3 - Add Methods to Employee Class

## Objective

Add behavioral methods to the Employee class that calculate values, perform operations, and return results based on object properties. This task demonstrates how methods extend class functionality beyond simple data storage.

---

## Context

You have been given an empty Python file: `Task 3 - Add Methods to Employee Class.py`

You will add methods to the Employee class from [Task 1](../Program%201%20-%20defining%20a%20class/Task%201%20-%20Create%20an%20Employee%20Class.md).

Your task is to implement the following methods:

---

## Requirements

### Method Implementations (FR1, FR2, FR3, FR4)

Implement the following methods in the Employee class:

#### 1. `get_full_name()` Method (FR1, FR2)
- **Purpose:** Return the employee's full name
- **Parameters:** None (besides `self`)
- **Return:** String in format "FirstName LastName"
- **Implementation:** `return f"{self.first_name} {self.last_name}"`

#### 2. `get_annual_salary()` Method (FR1, FR2)
- **Purpose:** Return the annual salary
- **Parameters:** None
- **Return:** Float value (same as self.salary)
- **Implementation:** `return self.salary`

#### 3. `calculate_monthly_salary()` Method (FR1, FR2, FR6)
- **Purpose:** Calculate monthly salary from annual
- **Parameters:** None
- **Return:** Float (annual salary / 12)
- **Implementation:** `return self.salary / 12`

#### 4. `apply_raise(raise_percentage)` Method (FR1, FR3, FR4, FR9)
- **Purpose:** Apply a percentage raise to salary
- **Parameters:** `raise_percentage` (float, 0-100)
- **Return:** New salary amount
- **Implementation:**
  - Validate raise_percentage is between 0-100
  - Calculate: `new_salary = self.salary * (1 + raise_percentage / 100)`
  - Update: `self.salary = new_salary`
  - Return new salary

#### 5. `get_employment_info()` Method (FR1, FR2, FR5)
- **Purpose:** Return formatted employment information
- **Parameters:** None
- **Return:** Multi-line string with all employment details
- **Implementation:** Format and return all properties as readable text

#### 6. `years_employed()` Method (FR1, FR2, FR6)
- **Purpose:** Calculate years since hire date
- **Parameters:** None
- **Return:** Integer (years of employment)
- **Implementation:**
  ```python
  from datetime import date
  today = date.today()
  years = (today - self.hire_date).days // 365
  return years
  ```

### Documentation (FR8)
- Add docstrings to each method
- Example: `"""Calculate and return months of salary (annual / 12)."""`

### Validation (FR9)
- `apply_raise()` should validate the raise percentage is reasonable (0-100)
- Raise an exception or return an error message if validation fails

---

## Implementation Steps

1. **Start with the Employee class from Task 1**
2. **Add each method inside the class:**
   ```python
   def get_full_name(self):
       """Return employee's full name."""
       return f"{self.first_name} {self.last_name}"
   ```

3. **Implement all 6 methods**
4. **Add docstrings to each method**
5. **Add validation to methods where appropriate**

---

## Testing Your Solution

```python
if __name__ == "__main__":
    from datetime import date
    
    emp = Employee(
        employee_id=101,
        first_name="John",
        last_name="Smith",
        salary=50000.00,
        department="IT",
        position="Developer",
        hire_date=date(2019, 3, 15)
    )
    
    # Test methods
    print(f"Full Name: {emp.get_full_name()}")
    print(f"Annual Salary: ${emp.get_annual_salary():.2f}")
    print(f"Monthly Salary: ${emp.calculate_monthly_salary():.2f}")
    print(f"Years Employed: {emp.years_employed()}")
    
    print(f"\nEmployment Info:\n{emp.get_employment_info()}")
    
    print(f"\nApplying 10% raise...")
    new_salary = emp.apply_raise(10)
    print(f"New Salary: ${new_salary:.2f}")
```

Expected output:
```
Full Name: John Smith
Annual Salary: $50000.00
Monthly Salary: $4166.67
Years Employed: 5

Employment Info:
Employee ID: 101
Name: John Smith
Position: Developer
Department: IT
Annual Salary: $50000.00
Hire Date: 2019-03-15

Applying 10% raise...
New Salary: $55000.00
```

---

## Functional Requirements Covered

- **FR1:** Define methods within the class to represent behaviors
- **FR2:** Use `self` parameter to access object properties
- **FR3:** Create methods with parameters (`apply_raise`)
- **FR4:** Implement methods that return values or modify state
- **FR5:** Demonstrate methods that retrieve/display information
- **FR6:** Show methods that calculate derived values
- **FR8:** Include docstrings for all methods
- **FR9:** Implement validation logic in methods

