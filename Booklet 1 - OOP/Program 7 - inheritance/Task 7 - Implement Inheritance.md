# Task 7 - Implement Inheritance

## Objective

Create a `Manager` class that inherits from the `Employee` class, adding manager-specific properties and methods. This task demonstrates class inheritance and method overriding.

---

## Context

You have been given an empty Python file: `Task 7 - Implement Inheritance.py`

You will use the Employee class from previous tasks as the parent class and create a Manager child class.

Your task is to:

1. Create a Manager class that inherits from Employee
2. Add manager-specific properties
3. Add manager-specific methods
4. Override parent methods where appropriate
5. Demonstrate polymorphism

---

## Requirements

### Parent Class (Employee)

The Employee class should have (from previous tasks):
- Properties: `_employee_id`, `_first_name`, `_last_name`, `_salary`, `_department`, `_position`, `_hire_date`
- Methods: getters, setters, `get_full_name()`, `calculate_monthly_salary()`, `years_employed()`

### Manager Class Definition (FR1, FR2, FR8)

Create a Manager class that:
```python
class Manager(Employee):
    """Represents a manager, extending Employee with management responsibilities."""
    
    def __init__(self, employee_id, first_name, last_name, salary, 
                 department, position, hire_date, team_size, budget):
        super().__init__(employee_id, first_name, last_name, salary, 
                        department, position, hire_date)
        self._team_size = team_size
        self._budget = budget
```

### Manager-Specific Properties (FR4)
- `_team_size` (int): Number of employees managed
- `_budget` (float): Annual budget for the department/team

### Manager-Specific Methods (FR5, FR9)

#### `get_team_size()` Method
- Return the number of employees managed

#### `set_team_size(size)` Method
- Validate: size >= 0
- Update team size

#### `get_budget()` Method
- Return the department budget

#### `set_budget(amount)` Method
- Validate: amount > 0
- Update budget

#### `get_budget_per_employee()` Method (FR9)
- Calculate: budget / team_size
- Handle division by zero gracefully

#### `add_team_member()` Method (FR9)
- Increment team_size by 1

#### `remove_team_member()` Method (FR9)
- Decrement team_size (validate team_size > 0)

### Method Overrides (FR5, FR6)

#### Override `get_info()` or `__str__()` (FR5, FR6)
```python
def get_info(self):
    """Return manager information including management details."""
    parent_info = super().get_info()  # Call parent's get_info()
    return f"{parent_info}\nManaging {self._team_size} employees\nBudget: ${self._budget:,.2f}"
```

#### Override `apply_raise()` (Optional) (FR5, FR6)
- Managers might get different raise logic
- For example: `raise_percentage *= 1.5` (managers get 50% more raise)

### Inheritance Test (FR3, FR7)
Demonstrate that Manager inherits from Employee:
```python
mgr = Manager(201, "Jane", "Doe", 80000, "IT", "IT Manager", 
              date(2015, 6, 1), team_size=5, budget=500000)

# Access inherited properties
print(f"Manager Name: {mgr.get_full_name()}")
print(f"Salary: ${mgr.get_salary():.2f}")
print(f"Monthly: ${mgr.calculate_monthly_salary():.2f}")

# Call Manager-specific methods
print(f"Team Size: {mgr.get_team_size()}")
print(f"Budget: ${mgr.get_budget():,.2f}")
```

---

## Implementation Steps

1. **Import parent class:**
   ```python
   from datetime import date
   # Import Employee class or define it
   ```

2. **Define Manager class that inherits:**
   ```python
   class Manager(Employee):
       """Manager class extending Employee."""
       
       def __init__(self, employee_id, first_name, last_name, salary, 
                    department, position, hire_date, team_size, budget):
           super().__init__(employee_id, first_name, last_name, salary, 
                           department, position, hire_date)
           self._team_size = team_size
           self._budget = budget
   ```

3. **Add manager properties and methods**

4. **Override parent method if needed:**
   ```python
   def get_info(self):
       parent_info = super().get_info()
       return f"{parent_info}\nTeam Members: {self._team_size}\nBudget: ${self._budget:,.2f}"
   ```

---

## Testing Your Solution

```python
if __name__ == "__main__":
    # Create employee and manager
    emp = Employee(100, "Bob", "Smith", 50000, "IT", "Developer", date(2018, 1, 15))
    mgr = Manager(200, "Alice", "Johnson", 80000, "IT", "Manager", date(2015, 6, 1), 
                  team_size=5, budget=500000)
    
    print("=== Employee ===")
    print(emp.get_info())
    
    print("\n=== Manager (Inherited from Employee) ===")
    print(mgr.get_full_name())
    print(f"Salary: ${mgr.get_salary():.2f}")
    print(f"Years Employed: {mgr.years_employed()}")
    
    print("\n=== Manager-Specific Info ===")
    print(mgr.get_info())
    print(f"Budget per Employee: ${mgr.get_budget_per_employee():,.2f}")
    
    print("\n=== Adding Team Member ===")
    mgr.add_team_member()
    print(f"New Team Size: {mgr.get_team_size()}")
    print(f"New Budget per Employee: ${mgr.get_budget_per_employee():,.2f}")
```

Expected output:
```
=== Employee ===
Employee: Bob Smith, Developer, IT, $50000.00

=== Manager (Inherited from Employee) ===
Alice Johnson
Salary: $80000.00
Years Employed: 9

=== Manager-Specific Info ===
Employee: Alice Johnson, Manager, IT, $80000.00
Managing 5 employees
Budget: $500,000.00
Budget per Employee: $100,000.00

=== Adding Team Member ===
New Team Size: 6
New Budget per Employee: $83,333.33
```

---

## Functional Requirements Covered

- **FR1:** Define parent class with common members
- **FR2:** Define child class inheriting from parent
- **FR3:** Child inherits all parent properties
- **FR4:** Child adds new manager-specific properties
- **FR5:** Child can override parent methods
- **FR6:** Child can call parent methods via `super()`
- **FR7:** Both can be displayed and used polymorphically
- **FR8:** Demonstrate inheritance syntax
- **FR9:** Show how child extends parent functionality
- **FR10:** Display output showing inherited and manager-specific behavior

