# Program 19 - Initial Connection

### Technical Explanation

This program demonstrates how a database connection is established and checked before any other database processing takes place. It begins by reading connection settings from environment variables, which shows the technical skill of using external configuration rather than hard-coding sensitive values directly into the program. It then validates those settings before attempting to connect, demonstrating defensive programming and input validation.

Once connected, the program creates a database cursor and runs a simple SQL query to retrieve the database server version. This demonstrates database connectivity, SQL execution, and the use of cursors to communicate with a relational database. The final cleanup stage shows resource management, as the cursor and connection are both closed safely after use. Overall, the main technical skills shown here are configuration management, validation, database connection handling, SQL querying, and safe cleanup of system resources.

---

## Analysis

### End User Requirements

1. The user wants to be able to check whether the system can connect to the database before running any other programs.
2. The user wants to see a clear message indicating whether the connection succeeded or failed.
3. If the connection succeeds, the user wants to see confirmation that the database is responding correctly.
4. If the connection fails, the user wants a helpful hint about what may have gone wrong so they can fix it.
5. The user wants to be told if the database settings have not been configured, rather than the program crashing silently.

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

FR9 Validate keyboard numeric input to ensure values are in the correct format and valid range.

FR10 Validate keyboard text input to ensure mandatory fields are non-empty and within allowed length.

FR11 Display clear success/failure messages and always close database resources safely.

FR12 Validate that selected database records exist before processing update or display actions.

FR13 Validate user-selected identifiers against expected data type and acceptable range.

FR14 Log or display meaningful error context to support troubleshooting of failed operations.

FR15 Ensure each transaction-based operation leaves the database in a consistent state.

---

## Design

### Query Design

This program uses one SQL query to confirm that the database connection is working correctly.

| Query | Purpose | SQL | Parameters | Expected Result |
|---|---|---|---|---|
| Get server version | Checks that the database is responding and returns version information | `SELECT VERSION();` | None | A single row containing the database server version |

### English Pseudocode

1. Start a procedure to test the database connection.
2. Display a message saying a connection check is being performed.
3. Read the database host, username, password, and database name from environment settings.
4. Check that all four environment variables have been set.
	1. If any are missing, display an error message naming the missing variables and stop.
5. Try to connect to the database using the validated settings.
6. If the connection is successful:
	1. Create a cursor.
	2. Run a query to get the database server version.
	3. Read the returned version value.
	4. Display a success message and display the version.
	5. Close the cursor and close the connection.
	6. Display a message confirming the connection was closed safely.
7. Otherwise:
	1. Display a failure message.
	2. Display a troubleshooting hint.

---

## Implementation

### SQA Reference Language

```text
Line 1: FUNCTION TestConnection()
Line 2:     SEND "Checking connection to external database..." TO DISPLAY

Line 3:     SET dbHost TO GETENV("DB_HOST")                                         [FR8]
Line 4:     SET dbUser TO GETENV("DB_USER")                                         [FR8]
Line 5:     SET dbPass TO GETENV("DB_PASS")                                         [FR8]
Line 6:     SET dbName TO GETENV("DB_NAME")                                         [FR8]

Line 7:     SET missing TO []
Line 8:     FOR EACH (varName, varValue) IN [("DB_HOST", dbHost), ("DB_USER", dbUser), ("DB_PASS", dbPass), ("DB_NAME", dbName)] DO
Line 9:         IF varValue = NULL OR varValue = "" THEN
Line 10:             APPEND varName TO missing
Line 11:         ENDIF
Line 12:     ENDFOR
Line 13:     IF LENGTH(missing) > 0 THEN
Line 14:         SEND "Configuration Error: Missing environment variable(s): " & JOIN(missing, ", ") TO DISPLAY   [FR8, FR11]
Line 15:         RETURN
Line 16:     ENDIF

Line 17:     SET conn TO MYSQLCONNECT(dbHost, dbUser, dbPass, dbName)               [FR6]

Line 18:     IF conn <> NULL AND conn.is_connected() = TRUE THEN
Line 19:         SET cursor TO conn.cursor()
Line 20:         cursor.execute("SELECT VERSION();")                                 [FR6]
Line 21:         SET version TO cursor.fetchone()

Line 22:         SEND "--- Connection Successful! ---" TO DISPLAY                     [FR11]
Line 23:         SEND "Database Server Version: " & version[0] TO DISPLAY             [FR7]

Line 24:         cursor.close()                                                      [FR11]
Line 25:         conn.close()                                                        [FR11]
Line 26:         SEND "Connection closed safely." TO DISPLAY                          [FR11]
Line 27:     ELSE
Line 28:         SEND "--- Connection Failed ---" TO DISPLAY                          [FR11]
Line 29:         SEND "Check your GitHub Secrets (Host, User, Pass) and Firewall settings." TO DISPLAY   [FR11, FR14]
Line 30:     ENDIF
Line 31: ENDFUNCTION

Line 32: CALL TestConnection()
```

The Python implementation is in [Program 19 - Initial Connection.py](./Program%2019%20-%20Initial%20Connection.py).

### Notes

- `MYSQLCONNECT(...)` represents the `mysql.connector.connect(...)` call used in Python.
- `GETENV(...)` represents reading values from the environment after the `.env` file has been loaded.
- The Python version includes exception handling for connection and query errors. SQA Reference Language does not map directly to Python `try/except`, so this version shows the main logical flow instead.

---

## Test plan

### Test Cases

| # | Functional Requirement | Test Description | Input / Conditions | Expected Output | Evidence |
|---|------------------------|------------------|--------------------|-----------------|----------|
| 1 | FR1 | Valid credentials loaded from environment | All four environment variables set correctly | Credentials read without error | Before evidence: capture the `.env` or environment values showing all four variables are present. After evidence: capture successful program startup with no configuration error message. |
| 2 | FR2 – one missing | One environment variable not set | DB_PASS unset | Error message naming DB_PASS displayed; program stops | Before evidence: capture environment settings showing `DB_PASS` missing while others exist. After evidence: capture output showing the named missing-variable error and no further connection attempt. |
| 3 | FR2 – all missing | No environment variables set | All four unset | Error message listing all four variables; program stops | Before evidence: capture environment settings showing none of the four variables are present. After evidence: capture output listing all missing variables and showing the program stops immediately. |
| 4 | FR3 | Progress message displayed | Program runs normally | "Checking connection to external database..." shown before connection attempt | Before evidence: capture the start of execution before any database result is printed. After evidence: capture output showing the progress message appears first. |
| 5 | FR4 | Successful database connection | Valid credentials | Connection established; no error raised | Before evidence: capture valid credentials and an available database service. After evidence: capture output showing the program reaches the success path without connection errors. |
| 6 | FR5 | Server version retrieved and displayed on success | Valid connection | "Database Server Version: x.x.x" shown | Before evidence: capture that the database server is running and reachable. After evidence: capture the returned version line from program output. |
| 7 | FR6 | Cursor and connection closed after success | Valid connection | No open handles remain after execution | Before evidence: capture that a connection is opened during execution if possible. After evidence: capture program completion plus any check showing no active cursor/connection remains. |
| 8 | FR7 | Safe-close confirmation message displayed | Valid connection | "Connection closed safely." shown | Before evidence: capture successful connection output before cleanup. After evidence: capture the explicit safe-close confirmation message. |
| 9 | FR8 – failure message | Invalid credentials provided | Wrong password or host | "--- Connection Failed ---" displayed | Before evidence: capture the incorrect host or password being used. After evidence: capture output showing the failure message. |
| 10 | FR8 – hint | Invalid credentials provided | Wrong password or host | Troubleshooting hint displayed | Before evidence: capture the same failed configuration used for the test. After evidence: capture the troubleshooting hint printed after the failure message. |