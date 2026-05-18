# Task 20 - Select All Students

## Objective

Write a Python program that connects to the Student database, retrieves all student records, stores them in an array of objects, and displays them in a formatted table. This task builds on the concepts from [Program 20 - Connect and Select](./Program%2020%20-%20Connect%20and%20Select.md), applying them to the Student database.

---

## Context

You have been given an empty Python file: `Task 20 - Select All Students.py`

Your task is to complete this file to:

1. Load database configuration from environment variables
2. Validate that all required configuration values are present
3. Establish a connection to the database
4. Execute a `SELECT` query to retrieve all students from the Students table
5. Create a Student class to represent student data
6. Convert query results into an array of Student objects
7. Display the results in a formatted table
8. Close the connection safely

---

## Student Class Requirements

You must define a `Student` class with properties for all columns in the Students table and provide getter methods for values that are displayed outside the class:

```python
class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, gender, 
                 enrollment_date, grade_level, enrollment_status, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.enrollment_date = enrollment_date
        self.grade_level = grade_level
        self.enrollment_status = enrollment_status
        self.email = email
        self.phone_number = phone_number
```

---

## Requirements

### Configuration & Connection (FR8, FR6)
- Load the `.env` file from the parent directory
- Read: `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`
- Validate all required variables are present
- Establish database connection with error handling

### Data Retrieval (FR6, FR2)
- Execute `SELECT * FROM Students;` to retrieve all records
- Get the count of rows returned
- Create a fixed-size array of Student objects matching the row count
- Loop through each result row and instantiate Student objects, storing them in array indices
- Handle SQL errors gracefully

### Display (FR7)
- Format and print the student data as a clear table with headers and aligned columns
- Use getter methods when reading values from each `Student` object for display
- Include all 10 student properties in the table
- Consider using column width formatting for readability
- Display a row count at the end (e.g., "Total: 54 students")

### Resource Management (FR11)
- Always close the cursor and connection safely in a `finally` block
- Display success/failure messages appropriately
- Show error details if connection or query fails

---

## Implementation Steps

1. **Imports:**
   ```python
   import os
   from pathlib import Path
   import mysql.connector
   from dotenv import load_dotenv
   from mysql.connector import Error
   from datetime import date
   ```

2. **Define the Student class** with all properties listed above

3. **Create a main function** (e.g., `select_all_students()`) that:
   - Prints a starting message
   - Loads and validates environment variables
   - Opens database connection
   - Executes SELECT query and captures row count
   - Creates fixed-size array of Student objects
   - Loops through cursor results, populating array
   - Displays formatted table
   - Closes resources safely

4. **Format the table output:**
   Consider using format strings or f-strings to align columns:
   ```python
   print(f"{student.get_student_id():<5} {student.get_first_name():<15} {student.get_last_name():<15} {student.get_grade_level():<10}")
   ```

5. **Add a `main` block:**
   ```python
   if __name__ == "__main__":
       select_all_students()
   ```

---

## Testing Your Solution

Run your program:
```bash
python "Task 20 - Select All Students.py"
```

Expected output structure:
```
Retrieving all students from database...
--- Connection Successful! ---

StudentID FirstName       LastName        DOB            Gender   GradeLevel Status   Email                      Phone
--------- --------------- --------------- -------------- -------- ---------- -------- ---------------------- ----------------
1         John            Doe             2011-03-15     Male     8          Active   john.doe@example.com  555-987-6543
2         Robert          Johnson         2010-01-10     Male     8          Active   robert.johnson@...    555-100-0002
...
[54 rows total]
```

---

## Reference

Use [Program 20 - Connect and Select](./Program%2020%20-%20Connect%20and%20Select.md) as your template. Key differences from Program 20:

- **Class name:** Change `Employee` to `Student`
- **Properties:** Use Student table columns (includes `gender`, `grade_level`, `enrollment_status`, `phone_number`)
- **Query:** Use `SELECT * FROM Students;` instead of Employees
- **Table display:** Format to show all 10 Student properties

---

## Functional Requirements Covered

- **FR1:** Define a Student class with appropriate properties
- **FR2:** Use an array of Student objects to store database records
- **FR6:** Connect to database and execute SELECT query
- **FR7:** Generate formatted table output to display results
- **FR8:** Validate environment configuration before database operations
- **FR11:** Display clear status messages and safe resource cleanup
