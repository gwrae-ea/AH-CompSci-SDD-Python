# Task 2 - Instantiate Employee Objects

## Objective

Write a Python program that creates multiple Employee objects, tests their properties, and demonstrates that each object stores independent data. This task practices instantiation, constructor use, and property access.

---

## Context

You have been given an empty Python file: `Task 2 - Instantiate Employee Objects.py`

You will use the `Employee` class from [Task 1](../Program%201%20-%20defining%20a%20class/Task%201%20-%20Create%20an%20Employee%20Class.py) or the example Employee class definition.

Your task is to:

1. Import or define the Employee class
2. Create at least 3 Employee objects with different data
3. Access and display properties from each object
4. Verify that objects are independent (changes to one do not affect others)
5. Display a summary showing all created employees

---

## Requirements

### Object Creation (FR1, FR2)
- Create at least 3 Employee objects
- Pass all required parameters (employee_id, first_name, last_name, salary, department, position, hire_date)
- Example employees might be: Developer, Manager, HR Officer, Salesperson, etc.

### Property Access (FR3, FR9)
- Access individual properties from each object using dot notation: `object.property_name`
- Examples: `emp1.first_name`, `emp2.salary`, `emp3.department`
- Display these accessed properties to verify they are stored correctly

### Independence Verification (FR4, FR10)
- Create at least two objects with different data
- Display both objects to show they maintain independent values
- Demonstrate that changing one object's property does not affect another (optional mutation test)

### Display Output (FR7, FR11)
- Display each employee using the object's `__str__` method
- Show summary information like total employees created
- Format output clearly with headers and alignment
- Use f-strings or format() for readable output

### Data Organization (FR6)
- Store employee objects in a list or array
- Loop through the collection to display all employees
- Show a count of total employees

---

## Implementation Steps

1. **Setup:**
   ```python
   from datetime import date
   from employee import Employee  # Or define it inline
   
   # Alternative: Define Employee class inline or import from Task 1
   ```

2. **Create employee objects:**
   ```python
   emp1 = Employee(
       employee_id=101,
       first_name="Alice",
       last_name="Johnson",
       salary=55000.00,
       department="Engineering",
       position="Senior Developer",
       hire_date=date(2018, 1, 15)
   )
   ```

3. **Store in a collection:**
   ```python
   employees = [emp1, emp2, emp3, ...]
   ```

4. **Display individual properties:**
   ```python
   print(f"Employee 1: {emp1.first_name} {emp1.last_name}")
   print(f"  Position: {emp1.position}")
   print(f"  Salary: ${emp1.salary:.2f}")
   ```

5. **Display all employees:**
   ```python
   print("\n=== All Employees ===")
   for emp in employees:
       print(emp)
   ```

6. **Optional: Test independence:**
   ```python
   # Modify one object's property
   emp1.salary = 60000.00
   # Verify emp2.salary is unchanged
   print(f"emp1.salary: {emp1.salary}, emp2.salary: {emp2.salary}")
   ```

---

## Testing Your Solution

Run your program and verify:

```
=== Employee Objects Created ===
Total Employees: 3

=== Individual Property Access ===
Employee 1: Alice Johnson
Position: Senior Developer
Salary: $55000.00

Employee 2: Bob Smith
Position: Manager
Salary: $48000.00

=== All Employees ===
Employee(id=101, name=Alice Johnson, position=Senior Developer, department=Engineering, salary=$55000.00, hire_date=2018-01-15)
Employee(id=102, name=Bob Smith, position=Manager, department=HR, salary=$48000.00, hire_date=2019-06-01)
Employee(id=103, name=Carol White, position=Analyst, department=Finance, salary=$42000.00, hire_date=2021-03-10)

=== Independence Test ===
Original emp1.salary: $55000.00
After modification: $60000.00
emp2.salary (unchanged): $48000.00
```

---

## Functional Requirements Covered

- **FR1:** Instantiate objects from the Employee class
- **FR2:** Pass parameters to constructor
- **FR3:** Access object properties using dot notation
- **FR4:** Verify object instances are independent
- **FR5:** Import/use class from another source
- **FR6:** Manage multiple instances correctly
- **FR7:** Display object data to verify creation
- **FR9:** Access individual properties
- **FR10:** Demonstrate property independence
- **FR11:** Display clear output with successful creation verification

