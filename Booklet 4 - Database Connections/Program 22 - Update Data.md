# Program 22 - Update Data

### Technical Explanation

This program demonstrates how an existing database record can be searched for and updated safely. It begins by validating the connection settings and opening a connection to the database, showing the technical skills of environment-based configuration, validation, and database connectivity. The program then asks the user for an employee ID and validates that it is a positive whole number before using it in a `SELECT` query to find the matching record. This demonstrates data validation, record lookup, and conditional logic.

Once the current record has been retrieved, the program displays the existing values and allows the user to enter replacement values while also allowing blank input to keep the current data. This demonstrates optional input handling, validation of text length and numeric values, and decision-making based on whether new input is provided. The `UPDATE` query is then executed using parameterised values, followed by transaction control to commit successful changes or roll them back if an error occurs. Overall, the technical skills shown are validation, record searching, conditional updates, parameterised SQL, transaction handling, and safe management of database resources.

---

## Analysis

### End User Requirements

1. The user wants to be able to update the details of an existing employee record in the database.
2. The user wants to be able to find the employee by typing their ID number.
3. The user wants to see the current values before making any changes, so they know what is already stored.
4. The user wants to be able to leave a field blank if they do not want to change it.
5. The user wants to be told immediately if they enter something invalid, so they can correct it.
6. The user wants to see a message confirming whether the record was updated or whether nothing changed.
7. The user wants to be told if the database settings have not been configured, rather than the program crashing silently.

### Functional Requirements

1. The system shall read database connection credentials (host, username, password, and database name) from environment variables.
2. The system shall validate that all four environment variables are set and non-empty. If any are missing, it shall display an error message identifying the missing variable(s) and stop execution.
3. If the connection fails, the system shall display an error message and stop execution.
4. The system shall prompt the user to enter an employee ID and validate that it is a whole number greater than 0. If invalid, it shall re-prompt until a valid value is supplied.
5. The system shall use a SELECT query to check that an employee with the given ID exists. If no record is found, it shall display an appropriate message and stop.
6. The system shall display the current values of the employee record before prompting for updates.
7. The system shall prompt for new name, position, salary, and department, allowing blank input to keep the existing value.
8. The system shall validate non-blank text fields against a maximum length. If exceeded, it shall display an error and re-prompt.
9. The system shall validate non-blank salary input as a positive number. If invalid or non-positive, it shall display an error and re-prompt.
10. The system shall execute an UPDATE query using parameterised values and commit the transaction.
11. If no rows were changed, the system shall display a message indicating no changes were made. Otherwise it shall display a success message.
12. If a database error occurs, the system shall display an error message and roll back the transaction.
13. The system shall close the cursor and database connection cleanly in all cases.

---

## Design

### Query Design

This program uses two parameterised SQL queries: one to find the existing employee record and one to update it.

| Query | Purpose | SQL | Parameters | Expected Result |
|---|---|---|---|---|
| Select employee by ID | Finds the employee record that matches the entered ID | `SELECT id, name, position, salary, department FROM Employees WHERE id = %s` | `employeeId` | One matching employee row or no row if the ID does not exist |
| Update employee by ID | Updates the selected employee record with the new values | `UPDATE Employees SET name = %s, position = %s, salary = %s, department = %s WHERE id = %s` | `newName`, `newPosition`, `newSalary`, `newDepartment`, `employeeId` | The matching employee row updated, or no rows changed if the values are unchanged |

### English Pseudocode

1. Start a procedure to update an existing employee record.
2. Read the database host, username, password, and database name from environment settings.
3. Check that all four environment variables have been set.
	1. If any are missing, display an error message naming the missing variables and stop.
4. Try to connect to the database using the validated settings.
5. If the connection fails:
	1. Display a connection error message.
	2. Stop the procedure.
6. Otherwise:
	1. Create a database cursor.
	2. Ask the user for an employee ID and validate that it is a whole number greater than 0.
	3. Use a SELECT query to fetch that employee record.
	4. If no record is found:
		1. Display a message that no employee exists with that ID.
		2. Stop the procedure.
	5. Display the current values.
	6. Ask for new name, position, salary, and department.
	7. Allow blank input to keep the existing value.
	8. Validate each non-blank text field length and salary value.
	9. Build an UPDATE query for the Employees table.
	10. Execute the UPDATE query and commit the transaction.
	11. If no rows were changed, display that no changes were made.
	12. Otherwise, display a success message.
	13. If a database error occurs:
		1. Display a database error message.
		2. Roll back the transaction.
	14. Close the cursor if it exists.
	15. Close the database connection.

---

## Implementation

The Python implementation is in [Program 22 - Update Data.py](./Program%2022%20-%20Update%20Data.py).

### SQA Reference Language

```text
Line 1: FUNCTION UpdateEmployee()
Line 2:     SET dbHost TO GETENV("DB_HOST")
Line 3:     SET dbUser TO GETENV("DB_USER")
Line 4:     SET dbPass TO GETENV("DB_PASS")
Line 5:     SET dbName TO GETENV("DB_NAME")

Line 6:     SET missing TO []
Line 7:     FOR EACH (varName, varValue) IN [("DB_HOST", dbHost), ("DB_USER", dbUser), ("DB_PASS", dbPass), ("DB_NAME", dbName)] DO
Line 8:         IF varValue = NULL OR varValue = "" THEN
Line 9:             APPEND varName TO missing
Line 10:         ENDIF
Line 11:     ENDFOR
Line 12:     IF LENGTH(missing) > 0 THEN
Line 13:         SEND "Configuration Error: Missing environment variable(s): " & JOIN(missing, ", ") TO DISPLAY
Line 14:         RETURN
Line 15:     ENDIF

Line 16:     SET conn TO MYSQLCONNECT(dbHost, dbUser, dbPass, dbName)
Line 17:     IF conn = NULL THEN
Line 18:         SEND "Connection Error" TO DISPLAY
Line 19:         RETURN
Line 20:     ENDIF

Line 21:     SET cursor TO NULL

Line 22:     TRY
Line 23:         SET cursor TO conn.cursor()

Line 24:         SEND "--- Update Employee Record ---" TO DISPLAY
Line 25:         SET employeeId TO VALIDATED_INTEGER_INPUT("Enter Employee ID to update: ")

Line 26:         SET selectQuery TO "SELECT id, name, position, salary, department FROM Employees WHERE id = %s"
Line 27:         cursor.execute(selectQuery, (employeeId))
Line 28:         SET employee TO cursor.fetchone()

Line 29:         IF employee = NULL THEN
Line 30:             SEND "No employee found with that ID." TO DISPLAY
Line 31:             RETURN
Line 32:         ENDIF

Line 33:         SEND "Leave blank to keep existing values." TO DISPLAY
Line 34:         SET newName TO OPTIONAL_VALIDATED_TEXT_INPUT("Enter New Name: ", employee.name)
Line 35:         SET newPosition TO OPTIONAL_VALIDATED_TEXT_INPUT("Enter New Position: ", employee.position)
Line 36:         SET newSalary TO OPTIONAL_VALIDATED_REAL_INPUT("Enter New Salary: ", employee.salary)
Line 37:         SET newDepartment TO OPTIONAL_VALIDATED_TEXT_INPUT("Enter New Department: ", employee.department)

Line 38:         SET updateQuery TO "UPDATE Employees SET name=%s, position=%s, salary=%s, department=%s WHERE id=%s"
Line 39:         SET values TO (newName, newPosition, newSalary, newDepartment, employeeId)
Line 40:         cursor.execute(updateQuery, values)
Line 41:         conn.commit()

Line 42:         IF cursor.rowcount = 0 THEN
Line 43:             SEND "No changes were made." TO DISPLAY
Line 44:         ELSE
Line 45:             SEND "Employee updated successfully." TO DISPLAY
Line 46:         ENDIF

Line 47:     CATCH DATABASEERROR
Line 48:         SEND "Database Error" TO DISPLAY
Line 49:         conn.rollback()

Line 50:     FINALLY
Line 51:         IF conn.is_connected() = TRUE THEN
Line 52:             IF cursor <> NULL THEN
Line 53:                 cursor.close()
Line 54:             ENDIF
Line 55:             conn.close()
Line 56:         ENDIF
Line 57:     ENDTRY
Line 58: ENDFUNCTION

Line 59: CALL UpdateEmployee()
```

### Notes

- `MYSQLCONNECT(...)` represents `mysql.connector.connect(...)` in the Python file.
- `GETENV(...)` represents reading values from environment variables after `.env` has been loaded.
- Validation helper routines in SQA-RL stand in for repeated input-check loops used in Python.

---

## Testing

### Test Cases

| # | Functional Requirement | Test Description | Input / Conditions | Expected Output | Evidence |
|---|------------------------|------------------|--------------------|-----------------|----------|
| 1 | FR1 | Valid credentials loaded from environment | All four environment variables set correctly | Credentials read without error | Before evidence: capture the configured environment variables. After evidence: capture program startup with no configuration error shown. |
| 2 | FR2 – one missing | One environment variable not set | DB_HOST unset | Error message naming DB_HOST displayed; program stops | Before evidence: capture environment settings showing `DB_HOST` missing. After evidence: capture the named missing-variable error and no update prompts. |
| 3 | FR2 – all missing | No environment variables set | All four unset | Error message listing all four variables; program stops | Before evidence: capture environment settings with all four variables absent. After evidence: capture output listing all missing variables and immediate stop. |
| 4 | FR3 | Connection failure stops execution | Invalid credentials | Error message displayed; program stops | Before evidence: capture the invalid credentials used. After evidence: capture the connection error and the absence of update processing. |
| 5 | FR4 – non-integer | Non-integer employee ID entered | Enter "abc" | Error message displayed; ID prompt repeated | Before evidence: capture the invalid text entered for employee ID. After evidence: capture the validation message and the repeated ID prompt. |
| 6 | FR4 – zero or negative | Zero or negative ID entered | Enter "0" or "-1" | Error message displayed; ID prompt repeated | Before evidence: capture the zero or negative ID entered. After evidence: capture the validation message and the repeated ID prompt. |
| 7 | FR4 – valid | Valid positive integer ID entered | Enter "3" | Value accepted; SELECT query runs | Before evidence: capture the valid ID entered and that it exists or will be searched. After evidence: capture progression to the record lookup stage without validation errors. |
| 8 | FR5 – not found | ID does not exist in Employees table | Enter an unused ID | "No employee found" message displayed; program stops | Before evidence: capture the table showing the ID does not exist. After evidence: capture the not-found message and no update prompt sequence. |
| 9 | FR5 – found | ID exists in Employees table | Enter a valid existing ID | Employee record retrieved | Before evidence: capture the existing employee row for that ID. After evidence: capture the program reaching the current-values display stage for that same record. |
| 10 | FR6 | Current values displayed before update prompts | Valid employee found | Current name, position, salary, department shown | Before evidence: capture the employee row in the database. After evidence: capture output showing the same current values before edits are entered. |
| 11 | FR7 | Blank input keeps existing value | Press Enter for name field | Original name retained in update | Before evidence: capture the original field value in the database. After evidence: capture the updated row showing that the original value is unchanged. |
| 12 | FR8 | Text field too long rejected | Enter a string exceeding max length | Error message displayed; field prompt repeated | Before evidence: capture the overlength text entered. After evidence: capture the validation message and the repeated field prompt. |
| 13 | FR9 – non-numeric salary | Non-numeric salary entered | Enter "abc" | Error message displayed; salary prompt repeated | Before evidence: capture the invalid salary value entered. After evidence: capture the salary validation message and repeated prompt. |
| 14 | FR9 – non-positive salary | Zero or negative salary entered | Enter "0" or "-100" | Error message displayed; salary prompt repeated | Before evidence: capture the zero or negative salary entered. After evidence: capture the validation message and repeated salary prompt. |
| 15 | FR10 | UPDATE query uses parameterised values | Valid input provided | UPDATE executed; no SQL injection risk | Before evidence: capture the original record values before update. After evidence: capture the database row after update showing only the intended changes. |
| 16 | FR11 – no changes | All fields left blank (kept same values) | Press Enter for all fields | "No changes were made." displayed | Before evidence: capture the record before the update attempt. After evidence: capture the no-changes message and the unchanged record after the run. |
| 17 | FR11 – updated | At least one field changed | Enter new name | "Employee updated successfully." displayed; record updated in DB | Before evidence: capture the original record values. After evidence: capture the success message and the changed row in the database. |
| 18 | FR12 | Database error triggers rollback | Simulate a constraint violation | Error message shown; transaction rolled back | Before evidence: capture the record before the failing update and the failure condition. After evidence: capture the error message and unchanged database row. |
| 19 | FR13 – success | Connection closed after successful update | Valid update | No open handles remain | Before evidence: capture that a connection is active during update processing. After evidence: capture completion plus any evidence that the connection/cursor is closed. |
| 20 | FR13 – error | Connection closed after database error | Simulated error | Connection and cursor still closed cleanly | Before evidence: capture the failing update setup. After evidence: capture the error path plus evidence that no connection/cursor remains open. |
