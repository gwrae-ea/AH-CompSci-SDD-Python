# Program 21 - Insert Data

### Technical Explanation

This program demonstrates how new data can be collected from a user and inserted into a database safely. It starts by validating the environment settings and establishing a database connection, showing the technical skills of configuration handling, validation, and database connectivity. The program then prompts the user for each required field and checks that the text fields are not blank and that salary is a valid number. This demonstrates user input handling, validation, and the use of repetition to re-prompt until correct data is entered.

After valid data has been collected, the program builds a parameterised SQL `INSERT` statement and executes it using a cursor. This demonstrates database insertion, parameterised queries, and transaction control through `commit()` and `rollback()`. The automatic setting of the hire date also shows how system-generated data can be combined with user input. Overall, the technical skills shown are validation, user interaction, selection and repetition constructs, database insertion, transaction handling, and safe cleanup of resources.

---

## Analysis

### End User Requirements

1. The user wants to be able to add a new employee to the database by entering their details interactively.
2. The user wants the system to ask for each piece of information clearly, one field at a time.
3. The user wants to be told immediately if they enter something invalid, so they can correct it without losing their other entries.
4. The user wants the hire date to be set automatically so they do not need to type it in.
5. The user wants to see a confirmation message once the employee has been added successfully.
6. The user wants to be told if the database settings have not been configured, rather than the program crashing silently.

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

FR6 Connect to the database to execute a query to validate connectivity and retrieve/update employee data as required.

FR7 Generate an interface to receive query input values and display formatted query output.

#### Additional functional requirements

The solution is required to:

FR8 Validate that required environment configuration values are present before attempting any database operation.

FR9 Validate the salary keyboard input: the value entered must be a positive floating-point number (greater than zero), matching the `salary float` column in the `Employees` table. Non-numeric input and values of zero or below must be rejected with an appropriate error message and re-prompted.

FR10 Validate the name, position, and department keyboard inputs: each value must be non-empty (blank input must be rejected) and must not exceed 20 characters, matching the `varchar(20)` definition of those columns in the `Employees` table. Invalid input must be rejected with an appropriate error message and re-prompted.

FR11 Display clear success and failure messages for all operational outcomes.

FR12 Set hireDate automatically to the current system date so the user is not required to enter it; the value is inserted directly into the `hireDate varchar(20)` column without any keyboard prompt.

FR13 Use a parameterised INSERT query to add the new record to the `Employees` table, ensuring no SQL injection is possible through user-supplied values.

FR14 Log or display meaningful error context to support troubleshooting of failed operations.

FR15 Commit the transaction on success, roll back on error, and always close the cursor and connection after execution.

---

## Design

### Query Design

This program uses one parameterised SQL query to add a new employee record safely to the database.

| Query | Purpose | SQL | Parameters | Expected Result |
|---|---|---|---|---|
| Insert new employee | Adds a new employee record to the Employees table | `INSERT INTO Employees (name, position, salary, department, hireDate) VALUES (%s, %s, %s, %s, %s)` | `name`, `position`, `salary`, `department`, `hireDate` | One new row inserted into the Employees table |

### English Pseudocode

1. Start a procedure to insert a new employee record.
2. Read the database host, username, password, and database name from environment settings.
3. Check that all four environment variables have been set.
	1. If any are missing, display an error message naming the missing variables and stop.
4. Try to connect to the database using the validated settings.
5. If the connection fails:
	1. Display a connection error message.
	2. Stop the procedure.
6. Otherwise:
	1. Create a database cursor.
	2. Display a heading to show that a new employee is being added.
	3. Ask the user for employee name; if blank, display an error and ask again until non-empty.
	4. Ask the user for job position; if blank, display an error and ask again until non-empty.
	5. Ask the user for salary; if non-numeric or negative, display an error and ask again until valid.
	6. Ask the user for department; if blank, display an error and ask again until non-empty.
	7. Set the hire date to today's date.
	8. Build an INSERT query for the Employees table.
	9. Create a values list from the user input and the hire date.
	10. Try to execute the INSERT query and commit the transaction.
	11. If the insert succeeds:
		1. Display a success message including the employee name.
	12. If a database error occurs:
		1. Display a database error message.
		2. Roll back the transaction.
	13. Close the cursor if it exists.
	14. Close the database connection.

---

## Implementation

### SQA Reference Language

```text
Line 1: FUNCTION InsertEmployee()
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

Line 24:         SEND "--- Add New Employee Record ---" TO DISPLAY                   [FR7]

Line 25:         SET name TO USERINPUT("Enter Employee Name: ").TRIM()              [FR7, FR10]
Line 26:         WHILE name = "" DO
Line 27:             SEND "Error: Employee name cannot be empty." TO DISPLAY
Line 28:             SET name TO USERINPUT("Enter Employee Name: ").TRIM()
Line 29:         ENDWHILE

Line 30:         SET position TO USERINPUT("Enter Job Position: ").TRIM()            [FR7, FR10]
Line 31:         WHILE position = "" DO
Line 32:             SEND "Error: Job position cannot be empty." TO DISPLAY
Line 33:             SET position TO USERINPUT("Enter Job Position: ").TRIM()
Line 34:         ENDWHILE

Line 35:         SET salary TO NULL
Line 36:         WHILE salary = NULL DO
Line 37:             TRY
Line 38:                 SET salary TO REAL(USERINPUT("Enter Salary: ").TRIM())      [FR7, FR9]
Line 39:                 IF salary < 0 THEN
Line 40:                     SEND "Error: Salary cannot be negative." TO DISPLAY
Line 41:                     SET salary TO NULL
Line 42:                 ENDIF
Line 43:             CATCH VALUEERROR
Line 44:                 SEND "Error: Please enter a valid number for the salary." TO DISPLAY
Line 45:             ENDTRY
Line 46:         ENDWHILE

Line 47:         SET department TO USERINPUT("Enter Department: ").TRIM()            [FR7, FR10]
Line 48:         WHILE department = "" DO
Line 49:             SEND "Error: Department cannot be empty." TO DISPLAY
Line 50:             SET department TO USERINPUT("Enter Department: ").TRIM()
Line 51:         ENDWHILE

Line 52:         SET hireDate TO TODAY()                                              [FR7]

Line 53:         SET query TO "INSERT INTO Employees (name, position, salary, department, hireDate) VALUES (%s, %s, %s, %s, %s)"  [FR5, FR6]
Line 54:         SET values TO (name, position, salary, department, hireDate)

Line 55:         cursor.execute(query, values)
Line 56:         conn.commit()                                                        [FR15]

Line 57:         SEND "Successfully added " & name & " to the Employees table." TO DISPLAY   [FR11]

Line 58:     CATCH DATABASEERROR
Line 59:         SEND "Database Error" TO DISPLAY                                   [FR11, FR14]
Line 60:         conn.rollback()                                                      [FR15]

Line 61:     FINALLY
Line 62:         IF conn.is_connected() = TRUE THEN
Line 63:             IF cursor <> NULL THEN
Line 64:                 cursor.close()                                              [FR15]
Line 65:             ENDIF
Line 66:             conn.close()                                                    [FR15]
Line 67:         ENDIF
Line 68:     ENDTRY
Line 69: ENDFUNCTION

Line 70: CALL InsertEmployee()
```

The Python implementation is in [Program 21 - Insert Data.py](./Program%2021%20-%20Insert%20Data.py).

### Notes

- `MYSQLCONNECT(...)` represents `mysql.connector.connect(...)` in the Python file.
- `GETENV(...)` represents reading values from environment variables after `.env` has been loaded.
- The Python version includes `try/except/finally`, so `TRY/CATCH/FINALLY` is used in SQA-RL style to show equivalent control flow.

---

## Test plan

### Test Cases

| # | Functional Requirement | Test Description | Input / Conditions | Expected Output | Evidence |
|---|------------------------|------------------|--------------------|-----------------|----------|
| 1 | FR8 – all valid | Valid credentials loaded from environment | All four environment variables set correctly | Credentials read without error | Before evidence: capture the configured environment variables. After evidence: capture program startup with no configuration error shown. |
| 2 | FR8 – one missing | One environment variable not set | DB_PASS unset | Error message naming DB_PASS displayed; program stops | Before evidence: capture environment settings showing `DB_PASS` missing. After evidence: capture the named missing-variable error and no insert prompts. |
| 3 | FR8 – all missing | No environment variables set | All four unset | Error message listing all four variables; program stops | Before evidence: capture environment settings with all four variables absent. After evidence: capture output listing all missing variables and immediate stop. |
| 4 | FR6/FR11 | Connection failure stops execution | Invalid credentials | Error message displayed; program stops | Before evidence: capture the invalid credentials used. After evidence: capture the connection error and the absence of input prompts. |
| 5 | FR7 | User prompted for all required fields | Valid connection | Prompts shown for name, position, salary, and department | Before evidence: capture successful connection and start of insert flow. After evidence: capture the sequence of prompts for all four user-entered fields. |
| 6 | FR10 – name empty | Employee name left blank | Press Enter with no input | Error message displayed; prompt repeated | Before evidence: capture the blank input submitted for name. After evidence: capture the validation message and the repeated name prompt. |
| 7 | FR10 – position empty | Job position left blank | Press Enter with no input | Error message displayed; prompt repeated | Before evidence: capture the blank position input. After evidence: capture the validation message and the repeated position prompt. |
| 8 | FR10 – department empty | Department left blank | Press Enter with no input | Error message displayed; prompt repeated | Before evidence: capture the blank department input. After evidence: capture the validation message and the repeated department prompt. |
| 9 | FR10 – name too long | Name exceeds 20 characters | Enter a 21-character name | Error message displayed; prompt repeated | Before evidence: capture the overlength name entered. After evidence: capture the validation message and the repeated name prompt. |
| 10 | FR9 – non-numeric | Non-numeric salary entered | Enter "abc" | Error message displayed; salary prompt repeated | Before evidence: capture the non-numeric salary value entered. After evidence: capture the validation message and the repeated salary prompt. |
| 11 | FR9 – negative | Negative salary entered | Enter "-500" | Error message displayed; salary prompt repeated | Before evidence: capture the negative salary entered. After evidence: capture the negative-value error and the repeated salary prompt. |
| 12 | FR9 – valid | Valid positive salary entered | Enter "30000" | Value accepted; no error | Before evidence: capture the valid salary input. After evidence: capture continuation to the next step without any validation message. |
| 13 | FR12 | Hire date set automatically to today | Valid connection and input | Hire date matches today's date; user not prompted for it | Before evidence: capture the current system date and the prompts shown to the user. After evidence: capture the inserted record showing today's date and no hire-date prompt. |
| 14 | FR13 | Record inserted using parameterised query | Valid input provided | INSERT executed with correct values; no SQL injection risk | Before evidence: capture that the record does not yet exist in the table. After evidence: capture the new row in the database with the expected values. |
| 15 | FR11/FR15 | Success message shown and transaction committed | Valid insert | Confirmation message displayed; record visible in Employees table | Before evidence: capture the table before insertion. After evidence: capture the success message and the new committed row in the table. |
| 16 | FR15 | Database error triggers rollback | Simulate a constraint violation | Error message shown; transaction rolled back | Before evidence: capture the table state and the failure condition. After evidence: capture the error message and unchanged table contents. |
| 17 | FR15 – success | Connection closed after success | Valid insert | No open handles remain after execution | Before evidence: capture that a connection is active during insert processing. After evidence: capture completion plus any check that the connection/cursor is closed. |
| 18 | FR15 – error | Connection closed after database error | Simulated error during insert | Connection and cursor still closed cleanly | Before evidence: capture the failing insert setup. After evidence: capture the error path plus evidence that no connection/cursor remains open. |

