# Task 23 - Delete Student Record

## Objective

Write a Python program that searches for a student by ID, displays their current information, asks for confirmation, and deletes the record from the Students database. This task builds on the concepts from [Program 23 - Delete Data](./Program%2023%20-%20Delete%20Data.md), applying them to the Student database.

---

## Context

You have been given an empty Python file: `Task 23 - Delete Student Record.py`

Your task is to complete this file to:

1. Load and validate database configuration
2. Establish a database connection
3. Prompt user for a student ID and validate it
4. Execute a `SELECT` query to find the student record
5. Display the student's current information
6. Ask the user to confirm deletion (Yes/No)
7. Execute a parameterised `DELETE` query
8. Commit the transaction or rollback on error
9. Confirm success or display appropriate messages
10. Close the connection safely

---

## Requirements

### Configuration & Connection (FR8, FR6)
- Load and validate environment variables: `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`
- Display error if config is incomplete
- Connect to database with error handling

### Student Lookup (FR12, FR13, FR6)
- Prompt user to enter a student ID
- Validate as positive integer (FR13)
- Execute `SELECT * FROM Students WHERE student_id = %s;` (FR6)
- Check if record exists (FR12)
- If not found, display message and exit gracefully

### Display Current Values (FR7)
- After finding student, display current values in readable format
- Show all key fields: ID, first name, last name, date of birth, grade level, enrollment status, email
- Use clear labels so user can verify the record before deletion

### Delete Confirmation (FR10, FR11)
- Prompt user with confirmation: `Are you sure you want to delete this student? (Yes/No):`
- Accept case-insensitive `yes/no` (or `y/n`)
- If invalid confirmation text is entered, re-prompt
- If user selects No, display cancellation message and exit with no DB change

### Delete Query (FR6)
- Execute parameterised DELETE query:
  - `DELETE FROM Students WHERE student_id = %s;`
- Use `%s` placeholder and tuple parameters (no string concatenation)
- Check affected row count after execution

### Transaction Control (FR15)
- Commit transaction on successful delete
- Rollback on error
- Ensure no partial/invalid database state remains

### User Feedback (FR11, FR14)
- Print clear status messages:
  - Lookup started
  - Record found/not found
  - Delete cancelled
  - Delete success
  - Database error details where relevant

### Resource Management (FR11)
- Use try/except/finally for safe cleanup
- Always close cursor and connection in finally block

---

## Implementation Steps

1. **Imports:**
   ```python
   import os
   from pathlib import Path
   import mysql.connector
   from dotenv import load_dotenv
   from mysql.connector import Error
   ```

2. **Set up environment loading:**
   - Use `Path(__file__).resolve().parent.parent.parent` to reach workspace root `.env`
   - Call `load_dotenv(dotenv_path=env_path)`

3. **Create helper validation functions:**
   ```python
   def get_positive_int(prompt):
       # Validate integer > 0
   
   def get_confirmation(prompt):
       # Accept yes/no and y/n
   ```

4. **Create main function** (e.g., `delete_student_record()`):
   - Validate environment config
   - Connect to DB
   - Prompt and validate student ID
   - Lookup student record
   - Show record details
   - Ask for confirmation
   - Run DELETE if confirmed
   - Commit/rollback and print result
   - Close resources safely

5. **Lookup query example:**
   ```python
   lookup_query = "SELECT * FROM Students WHERE student_id = %s;"
   cursor.execute(lookup_query, (student_id,))
   student = cursor.fetchone()
   if student is None:
       print("Student ID not found")
       return
   ```

6. **Delete query example:**
   ```python
   delete_query = "DELETE FROM Students WHERE student_id = %s;"
   cursor.execute(delete_query, (student_id,))
   conn.commit()
   ```

7. **Add a `main` block**

---

## Testing Your Solution

Run your program:
```bash
python "Task 23 - Delete Student Record.py"
```

Example interaction 1 (found and deleted):
```
--- Delete Student Record ---
Enter Student ID to delete: 12

Record found:
  Student ID: 12
  First Name: James
  Last Name: White
  Grade Level: 7
  Enrollment Status: Active

Are you sure you want to delete this student? (Yes/No): Yes
--- Student Deleted Successfully! ---
Connection closed safely.
```

Example interaction 2 (cancelled):
```
--- Delete Student Record ---
Enter Student ID to delete: 12

Record found:
  Student ID: 12
  First Name: James
  Last Name: White

Are you sure you want to delete this student? (Yes/No): No
Delete cancelled. No changes made.
Connection closed safely.
```

Example interaction 3 (not found):
```
--- Delete Student Record ---
Enter Student ID to delete: 9999
Student ID not found.
Connection closed safely.
```

---

## Reference

Use [Program 23 - Delete Data](./Program%2023%20-%20Delete%20Data.md) as your template. Key differences from Program 23:

- **Table:** Use `Students` instead of `Employees`
- **Primary key:** Use `student_id` instead of `id`
- **Display:** Show student-specific fields before confirmation
- **Messages:** Use student-focused wording

---

## Functional Requirements Covered

- **FR6:** Connect to database and execute SELECT/DELETE queries
- **FR7:** Generate input/output interface for delete workflow
- **FR8:** Validate environment configuration before operations
- **FR9:** Validate numeric input (student ID)
- **FR10:** Validate text input (confirmation)
- **FR11:** Display clear success/failure messages and safe cleanup
- **FR12:** Verify target record exists before delete
- **FR13:** Validate identifier input range/type
- **FR14:** Display meaningful error context
- **FR15:** Commit/rollback transaction control
