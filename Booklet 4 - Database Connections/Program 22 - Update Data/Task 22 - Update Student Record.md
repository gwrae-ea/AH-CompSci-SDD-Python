# Task 22 - Update Student Record

## Objective

Write a Python program that searches for a student by ID, displays their current information, allows selective field updates, and saves the changes to the database. This task builds on the concepts from [Program 22 - Update Data](./Program%2022%20-%20Update%20Data.md), applying them to the Student database.

---

## Context

You have been given an empty Python file: `Task 22 - Update Student Record.py`

Your task is to complete this file to:

1. Load and validate database configuration
2. Establish a database connection
3. Prompt user for a student ID and validate it
4. Execute a `SELECT` query to find the student record
5. Display the student's current information
6. Collect optional update values for each field
7. Execute a parameterised `UPDATE` query (only for non-blank fields)
8. Commit the transaction or rollback on error
9. Confirm success or display appropriate messages
10. Close the connection safely

---

## Requirements

### Configuration & Connection (FR8, FR6)
- Load and validate environment variables: `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`
- Display error if config incomplete
- Connect to database with error handling

### Student Lookup (FR12, FR13, FR6)
- Prompt user to enter a student ID
- Validate as positive integer (FR13)
- Execute `SELECT * FROM Students WHERE student_id = %s;` (FR6)
- Check if record exists (FR12)
- If not found, display message and exit gracefully

### Display Current Values (FR7)
- After finding student, display current values in readable format
- Show all 10 fields: ID, first name, last name, DOB, gender, enrollment date, grade level, status, email, phone
- Use clear labels so user knows what each value represents

### Optional Field Updates (FR10, FR9, FR13)
- For each field, prompt user to enter new value (OR leave blank to keep current)
- **Text fields (FR10):** first_name, last_name, enrollment_status, email, phone_number
  - Accept blank input (means "don't change")
  - If new value provided, validate length
  - Allow up to max length for that field
- **Numeric fields (FR9):** grade_level
  - Accept blank (means "don't change")
  - If new value provided, validate is integer in range 1-12
- **Date fields:** date_of_birth
  - Accept blank (means "don't change")
  - If new value provided, validate YYYY-MM-DD format
- **Enum fields:** gender
  - Accept blank (means "don't change")
  - If new value provided, validate is 'Male', 'Female', or 'Other'
- Note: enrollment_date cannot be changed (system field)

### Conditional Update (FR6, FR12)
- Build UPDATE query dynamically based on which fields have new values
- Only include fields where user provided new data
- Use parameterised query with `%s` placeholders
- Example: `UPDATE Students SET first_name = %s, grade_level = %s WHERE student_id = %s;`
- If no fields changed, show message "No changes made"

### Transaction Control (FR15)
- Commit transaction on successful update
- Rollback on error
- Always display connection status

### User Feedback (FR11, FR14)
- Print "Looking up student..."
- Show "Student found!" or "Student ID not found"
- After lookup, display current values clearly
- Display update prompts with current value shown in brackets: e.g., `New First Name [Current: Emma]: `
- On successful update: "--- Student Updated Successfully! ---"
- On error: Display error with meaningful context
- If no changes occurred: "--- No changes made ---"

### Resource Management (FR11)
- Use try/except/finally for safe cleanup
- Always close cursor and connection in finally block

---

## Implementation Steps

1. **Imports:**
   ```python
   import os
   from pathlib import Path
   from datetime import date
   import mysql.connector
   from dotenv import load_dotenv
   from mysql.connector import Error
   ```

2. **Create helper validation functions (similar to Task 21):**
   ```python
   def get_valid_text(prompt, max_length, current_value):
       # Returns either new text or None if user left blank
       # Format prompt to show current value
   
   def get_valid_grade_level(prompt, current_value):
       # Returns integer 1-12 or None if blank
   
   def get_valid_date(prompt, current_value):
       # Returns date object or None if blank
   ```

3. **Create main function** (e.g., `update_student_record()`):
   - Load and validate environment
   - Get and validate student ID
   - Lookup student
   - Display current values
   - Collect optional updates
   - Build dynamic UPDATE query
   - Execute and commit
   - Show results

4. **Lookup query:**
   ```python
   lookup_query = "SELECT * FROM Students WHERE student_id = %s;"
   cursor.execute(lookup_query, (student_id,))
   result = cursor.fetchone()
   if result is None:
       print("Student ID not found")
       return
   ```

5. **Dynamic UPDATE example:**
   ```python
   # Collect updates
   updates = {}
   new_first_name = get_valid_text("New First Name", 50, current_first_name)
   if new_first_name is not None:
       updates['first_name'] = new_first_name
   
   # Build query based on what changed
   if not updates:
       print("No changes made")
       return
   
   set_clause = ", ".join([f"{k} = %s" for k in updates.keys()])
   values = list(updates.values())
   values.append(student_id)
   
   update_query = f"UPDATE Students SET {set_clause} WHERE student_id = %s;"
   cursor.execute(update_query, values)
   conn.commit()
   ```

6. **Add a `main` block**

---

## Testing Your Solution

Run your program:
```bash
python "Task 22 - Update Student Record.py"
```

Example interaction 1 (student found and updated):
```
Looking up student...
Searching for student ID: 5

--- Student Found! ---
Current Values:
  Student ID: 5
  First Name: Jessica
  Last Name: Miller
  Date of Birth: 2014-02-14
  Gender: Female
  Enrollment Date: 2024-08-25
  Grade Level: 4
  Enrollment Status: Active
  Email: jessica.miller@example.com
  Phone: 555-100-0005

Enter updates (leave blank to keep current):
  New First Name [Jessica]: Jessie
  New Grade Level [4]: 5
  New Email [jessica.miller@example.com]: 

--- Student Updated Successfully! ---
Connection closed safely.
```

Example interaction 2 (student not found):
```
Looking up student...
Searching for student ID: 999
--- Student Not Found ---
Connection closed safely.
```

---

## Reference

Use [Program 22 - Update Data](./Program%2022%20-%20Update%20Data.md) as your template. Key differences from Program 22:

- **Fields:** Add Student-specific fields and types (gender enum, grade_level 1-12, phone_number, etc.)
- **Table:** Use `Students` instead of Employees
- **Query:** Use `SELECT * FROM Students WHERE student_id = %s;`
- **Validation:** Adjust ranges and constraints for Student fields

---

## Functional Requirements Covered

- **FR6:** Connect to database and execute SELECT/UPDATE queries
- **FR8:** Validate environment configuration before operations
- **FR9:** Validate numeric input (grade level 1-12)
- **FR10:** Validate text input (names, email, phone)
- **FR11:** Display success/failure messages and safe resource cleanup
- **FR12:** Verify student record exists before processing
- **FR13:** Validate user-selected identifiers (student ID)
- **FR14:** Display meaningful error context
- **FR15:** Commit/rollback transaction control
