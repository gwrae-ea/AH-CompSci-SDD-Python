# Program 20 - Connect and Select

### Technical Explanation

This program demonstrates how data can be read from a database and stored in an array of objects for later processing. After validating the environment settings and opening a connection, the program runs a `SELECT` query to retrieve all employee records. This shows the technical skills of database access, SQL query execution, and cursor use.

The returned rows are then processed by first reading how many rows were returned and creating a fixed-size array of the same length. Each row is converted into an `Employee` object and stored at the matching array index. This demonstrates object-oriented programming, array handling, indexed iteration, and the conversion of raw database records into structured program objects. Finally, the program formats and displays the results in tabular form, showing skills in data presentation and output formatting. Overall, this task brings together database processing, arrays, classes and objects, loops, and formatted output.

---

## Analysis

### End User Requirements

1. The user wants to be able to view all employee records stored in the database.
2. The user wants the records displayed in a clear, readable format with labelled columns.
3. The user wants to be told if the system cannot connect to the database, rather than it crashing.
4. The user wants to be told if the database settings have not been configured correctly.

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

FR9 Display all retrieved employee records in a clear tabular format with labelled column headings for id, name, salary, department, position, and hireDate, matching the column definitions in the `Employees` table.

FR10 Handle the case where the SELECT query returns zero rows by displaying no data rows and completing normally without error.

FR11 Display clear success and failure messages for all operational outcomes.

FR12 Use the row count returned by the SELECT query to correctly size the results array before populating it with Employee objects.

FR13 Map each returned database row to an Employee object stored at the corresponding index in the results array.

FR14 Log or display meaningful error context to support troubleshooting of failed operations.

FR15 Ensure the cursor and connection are always closed after execution, even if an error occurs during the query.

---

## Design

### Query Design

This program uses one SQL query to retrieve all employee records from the database before storing them in a fixed-size array of objects.

| Query | Purpose | SQL | Parameters | Expected Result |
|---|---|---|---|---|
| Select all employees | Retrieves every employee record from the Employees table | `SELECT * FROM Employees` | None | Zero or more rows containing full employee records |

### English Pseudocode

1. Define an Employee class with getter methods to hold and expose each row of employee data.
2. Start a procedure to select employee records from the database.
3. Read the database host, username, password, and database name from environment settings.
4. Check that all four environment variables have been set.
	1. If any are missing, display an error message naming the missing variables and stop.
5. Try to connect to the database using the validated settings.
6. If the connection fails:
	1. Display an error message.
	2. Stop the procedure.
7. Otherwise:
	1. Create a SQL query to select all rows from the Employees table.
	2. Create a cursor, execute the query, and fetch all rows.
	3. Read the number of rows returned.
	4. Create a fixed-size array of that length to hold Employee objects.
	5. For each index from 0 to number of rows minus 1:
		1. Create an Employee object from the row at that index.
		2. Store the Employee object at the same index in the array.
	6. Display column headings.
	7. For each Employee in the results array:
		1. Display that employee's details using getter methods.
	8. Close the cursor and close the database connection.

---

## Implementation

### SQA Reference Language

```text
Line 1: CLASS Employee                                                              [FR1]
Line 2:     FUNCTION __init__(id, name, salary, department, position, hireDate)
Line 3:         SET self.id TO id
Line 4:         SET self.name TO name
Line 5:         SET self.salary TO salary
Line 6:         SET self.department TO department
Line 7:         SET self.position TO position
Line 8:         SET self.hireDate TO hireDate
Line 9:     ENDFUNCTION
Line 10: ENDCLASS

Line 11: FUNCTION SelectEmployees()
Line 12:     SET dbHost TO GETENV("DB_HOST")                                         [FR8]
Line 13:     SET dbUser TO GETENV("DB_USER")                                         [FR8]
Line 14:     SET dbPass TO GETENV("DB_PASS")                                         [FR8]
Line 15:     SET dbName TO GETENV("DB_NAME")                                         [FR8]

Line 16:     SET missing TO []
Line 17:     FOR EACH (varName, varValue) IN [("DB_HOST", dbHost), ("DB_USER", dbUser), ("DB_PASS", dbPass), ("DB_NAME", dbName)] DO
Line 18:         IF varValue = NULL OR varValue = "" THEN
Line 19:             APPEND varName TO missing
Line 20:         ENDIF
Line 21:     ENDFOR
Line 22:     IF LENGTH(missing) > 0 THEN
Line 23:         SEND "Configuration Error: Missing environment variable(s): " & JOIN(missing, ", ") TO DISPLAY   [FR8, FR11]
Line 24:         RETURN
Line 25:     ENDIF

Line 26:     SET conn TO MYSQLCONNECT(dbHost, dbUser, dbPass, dbName)               [FR6]
Line 27:     IF conn = NULL OR conn.is_connected() = FALSE THEN
Line 28:         SEND "Connection failed" TO DISPLAY                                 [FR11]
Line 29:         RETURN
Line 30:     ENDIF

Line 31:     SET query TO "SELECT * FROM Employees"                                  [FR6]
Line 32:     SET cursor TO conn.cursor()
Line 33:     cursor.execute(query)
Line 34:     SET dbRows TO cursor.fetchall()

Line 35:     SET numRows TO LENGTH(dbRows)
Line 36:     SET results TO ARRAY OF SIZE numRows                                    [FR2]
Line 37:     FOR i FROM 0 TO numRows - 1 DO
Line 38:         SET results[i] TO NEW Employee(dbRows[i][0], dbRows[i][1], dbRows[i][2], dbRows[i][3], dbRows[i][4], dbRows[i][5])   [FR1, FR2]
Line 39:     ENDFOR

Line 40:     SEND "id        name                salary      dept                          position                      date" TO DISPLAY   [FR7]
Line 41:     FOR EACH worker IN results DO
Line 42:         SEND worker.get_id(), worker.get_name(), worker.get_salary(), worker.get_department(), worker.get_position(), worker.get_hire_date() TO DISPLAY   [FR7]
Line 43:     ENDFOR

Line 44:     cursor.close()                                                          [FR11]
Line 45:     conn.close()                                                            [FR11]
Line 46: ENDFUNCTION

Line 47: CALL SelectEmployees()
```

The Python implementation is in [Program 20 - Connect and Select.py](./Program%2020%20-%20Connect%20and%20Select.py).

### Notes

- `MYSQLCONNECT(...)` represents `mysql.connector.connect(...)` in the Python file.
- `GETENV(...)` represents reading values from environment variables after `.env` has been loaded.
- The Python version includes `try/except/finally` for database error handling and safe cleanup.

---

## Test plan

### Test Cases

| # | Functional Requirement | Test Description | Input / Conditions | Expected Output | Evidence |
|---|------------------------|------------------|--------------------|-----------------|----------|
| 1 | FR8 – all valid | Valid credentials loaded from environment | All four environment variables set correctly | Credentials read without error | Before evidence: capture the configured environment variables. After evidence: capture program startup with no configuration error. |
| 2 | FR8 – one missing | One environment variable not set | DB_NAME unset | Error message naming DB_NAME displayed; program stops | Before evidence: capture environment settings showing `DB_NAME` is missing. After evidence: capture output naming the missing variable and showing no query runs. |
| 3 | FR8 – all missing | No environment variables set | All four unset | Error message listing all four variables; program stops | Before evidence: capture environment settings with none of the variables present. After evidence: capture output listing all missing variables and immediate termination. |
| 4 | FR6 – connected | Successful database connection | Valid host, user, password, and database name | Connection established; no error raised | Before evidence: capture valid credentials and a reachable database. After evidence: capture output showing the program proceeds to data retrieval without connection errors. |
| 5 | FR6/FR11 – failure | Connection failure stops execution | Invalid or missing credentials | Error message displayed; program stops | Before evidence: capture the bad credentials or unavailable host. After evidence: capture the connection error output and absence of table data. |
| 6 | FR6 – rows returned | SELECT query returns all employee rows | Employees table contains data | All rows fetched from the database | Before evidence: capture the current rows in the `Employees` table. After evidence: capture displayed results matching those stored rows. |
| 7 | FR12 – row count | Row count read correctly from query result | Query returns 5 rows | Results array created with 5 slots | Before evidence: capture evidence that the table contains 5 rows. After evidence: capture displayed records and evidence that the array was sized for 5 items. |
| 8 | FR10 – empty table | No rows in Employees table | Table is empty | No data rows displayed; program completes normally | Before evidence: capture the empty `Employees` table. After evidence: capture output showing headings only with no employee rows printed. |
| 9 | FR13 | Each row mapped to an Employee object by index | Rows returned from query | results[i] holds Employee with correct field values for row i | Before evidence: capture one or more source rows from the database. After evidence: capture displayed values showing each object matches the row at the same index. |
| 10 | FR9 – headings | Records displayed with column headings | Valid data returned | Header row (id, name, salary, etc.) shown before records | Before evidence: capture the start of output before data rows appear. After evidence: capture the heading line shown above the records. |
| 11 | FR9 – data rows | Each employee's details displayed | Valid Employee objects in array | Each employee's id, name, salary, department, position, and hireDate shown | Before evidence: capture expected employee values from the database. After evidence: capture the printed table showing the same values in each row. |
| 12 | FR15 | Cursor and connection closed after use | Valid connection and query | No open handles remain after execution | Before evidence: capture that the program opens the database during processing. After evidence: capture completion plus any evidence that no connection/cursor remains active. |
| 13 | FR14/FR11 | Database error handled gracefully | Simulate a query error (e.g. table does not exist) | Appropriate error message displayed; resources closed | Before evidence: capture the condition causing the SQL failure. After evidence: capture the database error message and the absence of normal results output. |
