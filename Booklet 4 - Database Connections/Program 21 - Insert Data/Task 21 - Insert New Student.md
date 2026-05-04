# Task 21 - Insert New Student

## Objective

Write a Python program that collects student information from the user, validates the input, and inserts a new student record into the Students database. This task builds on the concepts from [Program 21 - Insert Data](./Program%2021%20-%20Insert%20Data.md), applying them to the Student database.

---

## Context

You have been given an empty Python file: `Task 21 - Insert New Student.py`

Your task is to complete this file to:

1. Load and validate database configuration
2. Establish a database connection
3. Collect student information from keyboard input
4. Validate each input field according to requirements
5. Automatically set the enrollment date to today
6. Execute a parameterised `INSERT` query
7. Commit the transaction or rollback on error
8. Display confirmation of success or failure
9. Close the connection safely

---

## Field Requirements

The program must collect and validate the following fields (matching Students table):

| Field | Type | Validation | Notes |
|-------|------|-----------|-------|
| First Name | VARCHAR(50) | Required, 1-50 characters | Prompt until valid |
| Last Name | VARCHAR(50) | Required, 1-50 characters | Prompt until valid |
| Date of Birth | DATE | Valid date (YYYY-MM-DD) | Must be before today |
| Gender | ENUM | 'Male', 'Female', or 'Other' | Case-insensitive selection |
| Grade Level | INT | Integer 1-12 | Validate numeric input FR9 |
| Enrollment Status | VARCHAR(20) | Text, max 20 chars | Required, typically 'Active' |
| Email | VARCHAR(100) | Optional email format | Validate if provided |
| Phone Number | VARCHAR(15) | Optional | Validate if provided |

---

## Requirements

### Configuration & Connection (FR8, FR6)
- Load and validate environment variables: `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`
- Display error if config incomplete
- Connect to database with error handling

### Input Collection (FR10, FR9, FR13)
- **Text validation (FR10):** Prompt for first name, last name, enrollment status
  - Check not empty
  - Check length <= max allowed
  - Re-prompt until valid
- **Numeric validation (FR9):** Prompt for grade level
  - Validate is integer
  - Validate in range 1-12
  - Re-prompt until valid
- **Date validation:** Accept date of birth in YYYY-MM-DD format
  - Validate date is before today
  - Re-prompt if invalid
- **Gender selection (FR13):** Offer choices: Male, Female, Other
  - Accept case-insensitive input
  - Validate against enum values
- **Optional fields:** Email and phone (optional but validate format if provided)

### Automatic Data (FR11)
- Set `enrollment_date` to today using `date.today()`
- Do not prompt user for this field

### Database Insertion (FR6, FR15)
- Build parameterised INSERT statement (use `%s` placeholders, NOT string concatenation)
- Example structure: `INSERT INTO Students (first_name, last_name, ...) VALUES (%s, %s, ...)`
- Execute with tuple of values in same order as column order in INSERT
- Commit transaction on success
- Rollback on any error

### User Feedback (FR11, FR14)
- Print "Adding new student to database..."
- On success: "--- Student Added Successfully! ---" and show the inserted details
- On error: Display error message with context
- Always show "Connection closed safely"

### Resource Management (FR11)
- Use try/except/finally for safe resource cleanup
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

2. **Create helper validation functions:**
   ```python
   def get_valid_text(prompt, max_length=50):
       while True:
           text = input(prompt).strip()
           if len(text) == 0:
               print(f"  Error: Field cannot be empty")
               continue
           if len(text) > max_length:
               print(f"  Error: Maximum {max_length} characters allowed")
               continue
           return text
   
   def get_valid_grade_level(prompt):
       while True:
           try:
               grade = int(input(prompt).strip())
               if grade < 1 or grade > 12:
                   print("  Error: Grade level must be between 1 and 12")
                   continue
               return grade
           except ValueError:
               print("  Error: Please enter a whole number")
   
   def get_valid_date(prompt):
       while True:
           try:
               date_str = input(prompt).strip()
               dob = date.fromisoformat(date_str)  # Accepts YYYY-MM-DD
               if dob >= date.today():
                   print("  Error: Date of birth must be before today")
                   continue
               return dob
           except ValueError:
               print("  Error: Please enter date in YYYY-MM-DD format")
   ```

3. **Create main insertion function** (e.g., `insert_new_student()`):
   - Load and validate environment
   - Collect validated input for each field
   - Insert with parameterised query
   - Commit/rollback based on result

4. **Data structure for insertion:**
   ```python
   student_data = (
       first_name,
       last_name,
       date_of_birth,
       gender,
       enrollment_date,  # Set to today
       grade_level,
       enrollment_status,
       email if email else None,
       phone_number if phone_number else None
   )
   ```

5. **INSERT query example:**
   ```python
   query = """INSERT INTO Students 
              (first_name, last_name, date_of_birth, gender, enrollment_date, 
               grade_level, enrollment_status, email, phone_number) 
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
   cursor.execute(query, student_data)
   conn.commit()
   ```

6. **Add a `main` block**

---

## Testing Your Solution

Run your program:
```bash
python "Task 21 - Insert New Student.py"
```

Example interaction:
```
Adding new student to database...
First Name: Emma
Last Name: Thompson
Date of Birth (YYYY-MM-DD): 2010-05-15
Gender (Male/Female/Other): Female
Grade Level (1-12): 8
Enrollment Status: Active
Email (optional): emma.thompson@example.com
Phone Number (optional): 555-123-4567

--- Student Added Successfully! ---
Connection closed safely.
```

---

## Reference

Use [Program 21 - Insert Data](./Program%2021%20-%20Insert%20Data.md) as your template. Key differences from Program 21:

- **Class/fields:** Add Student-specific fields (gender, grade_level, enrollment_status, phone_number)
- **Table:** Use `Students` instead of Employees
- **Validation:** Adjust for Student-specific field ranges (e.g., grade_level 1-12 instead of salary)
- **Query fields:** 9 columns from Students table

---

## Functional Requirements Covered

- **FR6:** Connect to database and execute INSERT query
- **FR8:** Validate environment configuration before operations
- **FR9:** Validate numeric input (grade level)
- **FR10:** Validate text input (names, status)
- **FR11:** Display success/failure messages and safe resource cleanup
- **FR13:** Validate input against acceptable ranges
- **FR14:** Display meaningful error context
- **FR15:** Commit/rollback transaction control
