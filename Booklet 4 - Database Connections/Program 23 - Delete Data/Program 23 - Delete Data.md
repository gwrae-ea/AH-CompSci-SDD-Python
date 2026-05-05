# Program 23 - Delete Data

### Technical Explanation

This program demonstrates how an existing database record can be located and deleted safely. It starts by validating the environment configuration and establishing a database connection. It then asks the user for an employee ID, validates the input, and uses a parameterised SELECT query to confirm that the target record exists.

If a matching record is found, the current record values are displayed to the user and explicit confirmation is requested before any deletion occurs. This helps prevent accidental data loss. The program then executes a parameterised DELETE query and commits the transaction. If an error occurs, the transaction is rolled back to keep the database consistent. Overall, the key technical skills shown are input validation, record lookup, delete confirmation, parameterised SQL, transaction management, and safe resource cleanup.

---

## Analysis

### End User Requirements

1. The user wants to delete an existing employee record from the database.
2. The user wants to select the record by employee ID.
3. The user wants to see the record before deletion so they can verify it is correct.
4. The user wants a confirmation step to avoid accidental deletes.
5. The user wants a clear success or failure message after the delete attempt.
6. The user wants the program to handle missing configuration and database errors safely.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Have an object-oriented solution with a developer defined class to represent employee data with appropriate properties and methods.

FR2 Use an array of objects to store employee records for processing and display.

FR3 Use a binary search algorithm.

FR4 Apply the algorithm in FR3 to the data structure in FR2 to locate a target employee record efficiently.

#### Integration

The solution is required to:

FR5 Have a database table to store employee records.

FR6 Connect to the database to execute a query to validate connectivity and retrieve/update/delete employee data as required.

FR7 Generate an interface to receive query input values and display formatted query output.

#### Additional functional requirements

The solution is required to:

FR8 Validate that required environment configuration values are present before attempting any database operation.

FR9 Validate the Employee ID keyboard input: the value entered must be a whole number (integer) greater than zero, matching the `id` field defined as `INT NOT NULL AUTO_INCREMENT` in the `Employees` table. Non-numeric input and values of zero or below must be rejected with an appropriate error message and re-prompted.

FR10 Validate the delete confirmation keyboard input: the value entered must be one of the accepted strings `y`, `yes`, `n`, or `no` (case-insensitive). Any other input must be rejected with an appropriate error message and re-prompted.

FR11 Display clear success, cancel, and error messages for all operational outcomes.

FR12 Confirm that a record matching the entered Employee ID exists in the `Employees` table before proceeding with deletion and display the matched record to the user for verification.

FR13 Log or display meaningful error context to support troubleshooting of failed operations.

FR14 Ensure each transaction-based operation leaves the database in a consistent state.

FR15 Always close the cursor and connection after execution, whether the delete succeeds, is cancelled, or encounters an error.

---

## Design

### Query Design

This program uses two parameterised SQL queries: one to locate the employee record and one to delete it.

| Query | Purpose | SQL | Parameters | Expected Result |
|---|---|---|---|---|
| Select employee by ID | Finds the employee record that matches the entered ID | `SELECT id, name, position, salary, department FROM Employees WHERE id = %s` | `employeeId` | One matching employee row or no row if the ID does not exist |
| Delete employee by ID | Deletes the selected employee record | `DELETE FROM Employees WHERE id = %s` | `employeeId` | One row deleted, or no rows if nothing matched |

### English Pseudocode

1. Start a procedure to delete an existing employee record.
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
   5. Display the current record values.
   6. Ask for confirmation before delete.
   7. If confirmation is No:
      1. Display cancellation message.
      2. Stop the procedure.
   8. Execute the DELETE query for the selected employee ID.
   9. Commit the transaction.
   10. If no rows were deleted, display no-delete message.
   11. Otherwise, display success message.
   12. If a database error occurs:
      1. Display a database error message.
      2. Roll back the transaction.
   13. Close the cursor if it exists.
   14. Close the database connection.

---

## Implementation

### SQA Reference Language

```text
Line 1: FUNCTION DeleteEmployee()
Line 2:     SET dbHost TO GETENV("DB_HOST")                                         [FR8]
Line 3:     SET dbUser TO GETENV("DB_USER")                                         [FR8]
Line 4:     SET dbPass TO GETENV("DB_PASS")                                         [FR8]
Line 5:     SET dbName TO GETENV("DB_NAME")                                         [FR8]

Line 6:     SET missing TO []
Line 7:     FOR EACH (varName, varValue) IN [("DB_HOST", dbHost), ("DB_USER", dbUser), ("DB_PASS", dbPass), ("DB_NAME", dbName)] DO
Line 8:         IF varValue = NULL OR varValue = "" THEN
Line 9:             APPEND varName TO missing
Line 10:         ENDIF
Line 11:     ENDFOR
Line 12:     IF LENGTH(missing) > 0 THEN
Line 13:         SEND "Configuration Error: Missing environment variable(s): " & JOIN(missing, ", ") TO DISPLAY   [FR8, FR11]
Line 14:         RETURN
Line 15:     ENDIF

Line 16:     SET conn TO MYSQLCONNECT(dbHost, dbUser, dbPass, dbName)               [FR6]
Line 17:     IF conn = NULL THEN
Line 18:         SEND "Connection Error" TO DISPLAY                                 [FR11]
Line 19:         RETURN
Line 20:     ENDIF

Line 21:     SET cursor TO NULL

Line 22:     TRY
Line 23:         SET cursor TO conn.cursor()

Line 24:         SEND "--- Delete Employee Record ---" TO DISPLAY
Line 25:         SET employeeId TO VALIDATED_INTEGER_INPUT("Enter Employee ID to delete: ")   [FR7, FR9]

Line 26:         SET selectQuery TO "SELECT id, name, position, salary, department FROM Employees WHERE id = %s"   [FR6, FR12]
Line 27:         cursor.execute(selectQuery, (employeeId))
Line 28:         SET employee TO cursor.fetchone()

Line 29:         IF employee = NULL THEN
Line 30:             SEND "No employee found with that ID." TO DISPLAY               [FR11, FR12]
Line 31:             RETURN
Line 32:         ENDIF

Line 33:         SEND "Display current record values" TO DISPLAY                     [FR7]
Line 34:         SET confirmDelete TO VALIDATED_TEXT_INPUT("Confirm delete (Yes/No): ")   [FR10]
Line 35:         IF confirmDelete = "No" THEN
Line 36:             SEND "Delete cancelled. No changes made." TO DISPLAY            [FR11]
Line 37:             RETURN
Line 38:         ENDIF

Line 39:         SET deleteQuery TO "DELETE FROM Employees WHERE id = %s"            [FR6]
Line 40:         cursor.execute(deleteQuery, (employeeId))
Line 41:         conn.commit()                                                        [FR14]

Line 42:         IF cursor.rowcount = 0 THEN
Line 43:             SEND "No record was deleted." TO DISPLAY
Line 44:         ELSE
Line 45:             SEND "Employee deleted successfully." TO DISPLAY                 [FR11]
Line 46:         ENDIF

Line 47:     CATCH DATABASEERROR
Line 48:         SEND "Database Error" TO DISPLAY                                   [FR11, FR13]
Line 49:         conn.rollback()                                                      [FR14]

Line 50:     FINALLY
Line 51:         IF conn.is_connected() = TRUE THEN
Line 52:             IF cursor <> NULL THEN
Line 53:                 cursor.close()                                              [FR15]
Line 54:             ENDIF
Line 55:             conn.close()                                                    [FR15]
Line 56:         ENDIF
Line 57:     ENDTRY
Line 58: ENDFUNCTION

Line 59: CALL DeleteEmployee()
```

The Python implementation is in [Program 23 - Delete Data.py](./Program%2023%20-%20Delete%20Data.py).

### Notes

- `MYSQLCONNECT(...)` represents `mysql.connector.connect(...)` in the Python file.
- `GETENV(...)` represents reading values from environment variables after `.env` has been loaded.
- The confirmation prompt is used to reduce accidental record deletion.

---

## Test plan

### Test Cases

| # | Functional Requirement | Test Description | Input / Conditions | Expected Output | Evidence |
|---|------------------------|------------------|--------------------|-----------------|----------|
| 1 | FR8 | Valid credentials loaded from environment | All four environment variables set correctly | Credentials read without error | Before evidence: capture configured environment variables. After evidence: capture startup without configuration error. |
| 2 | FR8 | One environment variable missing | DB_HOST unset | Error naming DB_HOST displayed; program stops | Before evidence: capture DB_HOST missing. After evidence: capture missing-variable error and stop. |
| 3 | FR11 | Connection failure handling | Invalid DB credentials | Connection error shown; program stops | Before evidence: capture invalid credentials used. After evidence: capture connection error and no delete flow. |
| 4 | FR9 | Non-integer ID rejected | Enter "abc" | Validation error shown; prompt repeated | Before evidence: capture invalid input. After evidence: capture repeated ID prompt. |
| 5 | FR9 | Zero/negative ID rejected | Enter "0" or "-1" | Validation error shown; prompt repeated | Before evidence: capture invalid numeric input. After evidence: capture repeated ID prompt. |
| 6 | FR12 | ID not found | Enter unused ID | Not-found message; program stops | Before evidence: capture table showing ID absent. After evidence: capture not-found message. |
| 7 | FR7 | Existing record displayed | Enter existing ID | Current record values displayed | Before evidence: capture row in table. After evidence: capture matching values in output. |
| 8 | FR10 | Confirmation validation | Enter invalid confirmation text | Prompt repeats until Yes/No | Before evidence: capture invalid text. After evidence: capture validation message and repeat prompt. |
| 9 | FR11 | Delete cancelled by user | Enter existing ID then "No" | Cancel message shown; no delete occurs | Before evidence: capture record exists pre-run. After evidence: capture cancellation and unchanged row. |
| 10 | FR6/FR14 | Delete confirmed and committed | Enter existing ID then "Yes" | Success message; row removed from DB | Before evidence: capture target row present. After evidence: capture success message and row absence. |
| 11 | FR13/FR14 | Database error rollback | Simulate delete failure | Error shown; transaction rolled back | Before evidence: capture pre-delete state and failure setup. After evidence: capture error and unchanged state. |
| 12 | FR15 | Resource cleanup on all paths | Success/cancel/error paths | Cursor and connection closed cleanly | Before evidence: capture active connection during process. After evidence: capture completion with safe closure behavior. |
