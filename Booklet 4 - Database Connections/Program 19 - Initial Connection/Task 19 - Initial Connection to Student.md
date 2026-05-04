# Task 19 - Initial Connection to Student

## Objective

Write a Python program that tests the connection to a **Student** database and demonstrates successful database connectivity. This task builds on the concepts from [Program 19 - Initial Connection](./Program%2019%20-%20Initial%20Connection.md), but applies them to a different database table.

---

## Context

You have been given an empty Python file: `Task 19 - Initial Connection to Student.py`

Your task is to complete this file to:

1. Load database configuration from environment variables (from the `.env` file)
2. Validate that all required configuration values are present
3. Establish a connection to the database
4. Execute a query to confirm the database is responding
5. Provide clear status messages to the user
6. Close the connection safely

---

## Student Database Schema

The Students table has the following structure:

| Column | Type | Description |
|--------|------|-------------|
| `student_id` | INT | Unique student identifier (auto-increment) |
| `first_name` | VARCHAR(50) | Student's first name |
| `last_name` | VARCHAR(50) | Student's last name |
| `date_of_birth` | DATE | Student's date of birth |
| `gender` | ENUM('Male','Female','Other') | Student's gender |
| `enrollment_date` | DATE | Date student enrolled |
| `grade_level` | INT | Grade level (1-12) |
| `enrollment_status` | VARCHAR(20) | Enrollment status (e.g., 'Active') |
| `email` | VARCHAR(100) | Student's email address |
| `phone_number` | VARCHAR(15) | Student's phone number |

---

## Requirements

### Configuration Management (FR8)
- Load the `.env` file located in the parent directory (use `Path` and `load_dotenv` as shown in Program 19)
- Read these environment variables: `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`
- Check that all required variables are present before attempting connection
- If any are missing, display an error message listing which ones and exit gracefully

### Database Connection (FR6)
- Use `mysql.connector` to connect to the database
- Handle connection errors gracefully with try/except blocks
- Execute a SQL query to verify the connection is working (e.g., `SELECT COUNT(*) FROM Student;`)

### User Feedback (FR11)
- Display a message indicating the status check is starting
- If successful: show a confirmation message and display the query result (e.g., the number of students or server version)
- If configuration is missing: show which environment variables are missing
- If connection fails: show the error message and troubleshooting guidance
- Always close the connection and cursor safely in a `finally` block

---

## Implementation Steps

1. **Import required modules** at the top of the file:
   - `os`
   - `Path` from `pathlib`
   - `mysql.connector`
   - `load_dotenv` from `dotenv`
   - `Error` from `mysql.connector`

2. **Set up environment loading:**
   - Use `Path(__file__).resolve().parent.parent.parent` to navigate to the workspace root where `.env` is stored
   - Call `load_dotenv(dotenv_path=env_path)`

3. **Create a main function** (e.g., `test_student_connection()`) that:
   - Prints a starting message
   - Reads and validates environment variables
   - Attempts connection with error handling
   - Executes a test query on the Student table
   - Closes resources safely

4. **Add a `main` block:**
   ```python
   if __name__ == "__main__":
       test_student_connection()
   ```

---

## Testing Your Solution

To test your program:

1. Ensure your `.env` file contains valid database credentials:
   ```
   DB_HOST=your_host
   DB_USER=your_user
   DB_PASS=your_password
   DB_NAME=your_database
   ```

2. Run your program:
   ```bash
   python "Task 19 - Initial Connection to Student.py"
   ```

3. You should see output like:
   - **Success case:** `Checking connection to external database... --- Connection Successful! --- Number of Students: X Connection closed safely.`
   - **Missing config case:** `Configuration Error: Missing environment variable(s): DB_PASS, DB_NAME`
   - **Connection failure case:** `Connection Error: [error details] --- Connection Failed --- Check your GitHub Secrets...`

---

## Reference

Use [Program 19 - Initial Connection](./Program%2019%20-%20Initial%20Connection.md) as a template. The structure is identical; only the database table and query change. You may adapt the code directly, changing:
- Function name from `test_connection()` to something like `test_student_connection()`
- The query from `SELECT VERSION();` to a query on the Student table (e.g., `SELECT COUNT(*) FROM Student;`)
- Output messages to reference "Students" instead of "Database Server Version"

---

## Functional Requirements Covered

- **FR6:** Connect to the database and execute a query
- **FR8:** Validate environment configuration before database operations
- **FR11:** Provide clear status feedback during program execution

