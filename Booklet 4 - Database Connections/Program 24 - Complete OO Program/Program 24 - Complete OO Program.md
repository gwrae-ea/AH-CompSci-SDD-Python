# Program 24 - Complete OO Program

### Technical Explanation

This program combines object-oriented design, database integration, validation, and a standard algorithm into one complete solution. Employee records are read from the `Employees` table and converted into an array of `Employee` objects. The class uses encapsulation with private attributes and explicit getter/setter methods.

The program applies an insertion sort algorithm to the employee object array by salary (highest first), then asks the user for filter criteria and displays matching records in a formatted table. A pay-rise percentage is then applied to the matched objects using setter methods, demonstrating controlled updates to object state. The SQL query deliberately avoids `ORDER BY` so sorting is handled in Python.

---

## Analysis

### End User Requirements

EU1. The user wants to load employee data from the database into the program.
EU2. The user wants employee records processed using an object-oriented approach.
EU3. The user wants a sorted and filtered employee list based on their inputs.
EU4. The user wants clear output, validation messages, and safe program behaviour.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Have an object-oriented solution with a developer defined class to represent employee data, including getter and setter methods.

FR2 Use an array of objects to store and process employee data loaded from the database.

FR3 Use an insertion sort algorithm.

FR4 Apply the algorithm in FR3 to the data structure in FR2 to sort employee objects by salary.

#### Integration

The solution is required to:

FR5 Have a database table to store employee records.

FR6 Connect to the database to execute a query to read employee rows.

FR7 Generate an interface to receive query input values and display formatted query output.

#### Additional functional requirements

The solution is required to:

FR8 Validate that required environment configuration values are present before database actions.

FR9 Validate numeric keyboard input for minimum salary and pay-rise percentage.

FR10 Validate text keyboard input for department criteria.

FR11 Display clear status, success, and error messages.

FR12 Filter records based on user-entered department and minimum salary values.

FR13 Provide meaningful context when row validation or runtime errors occur.

FR14 Handle runtime errors safely so processing remains stable.

FR15 Always close database resources after execution.

---

## Design

### Query Design

| Query | Purpose | SQL | Parameters | Expected Result |
|---|---|---|---|---|
| Select employees | Read all rows from Employees table | `SELECT id, name, salary, department, position, hireDate FROM Employees` | None | Array of employee rows for object creation |

### English Pseudocode

1. Load environment settings and validate required database values.
2. Connect to the database and read rows from `Employees`.
3. Convert each row into an `Employee` object using class setter methods.
4. Apply insertion sort to the array of objects by salary descending.
5. Ask the user for department, minimum salary, and pay-rise percentage.
6. Filter matching employee objects using the entered criteria.
7. Display matching records in formatted output.
8. Apply salary increase to matching objects using `set_salary()`.
9. Display updated matching records.
10. Close the database connection.

---

## Implementation

### SQA Reference Language

```text
Line 1: FUNCTION RunProgram24()
Line 2:     SET dbHost, dbUser, dbPass, dbName TO GETENV(...)                          [FR8]
Line 3:     IF any required value missing THEN DISPLAY config error and RETURN          [FR8, FR11]
Line 4:     SET conn TO MYSQLCONNECT(dbHost, dbUser, dbPass, dbName)                   [FR6]
Line 5:     IF conn = NULL THEN DISPLAY connection error and RETURN                     [FR11]
Line 6:     SET rows TO EXECUTE_QUERY("SELECT id, name, salary, department, position, hireDate FROM Employees") [FR6]
Line 7:     SET employeeArray TO []                                                     [FR2]
Line 8:     FOR EACH row IN rows DO
Line 9:         CREATE Employee object using constructor and setter validation           [FR1, FR2]
Line 10:        APPEND object TO employeeArray                                           [FR2]
Line 11:    ENDFOR
Line 12:    CALL InsertionSortBySalary(employeeArray)                                   [FR3, FR4]
Line 13:    SET departmentInput TO VALIDATED_TEXT_INPUT()                               [FR7, FR10]
Line 14:    SET minimumSalaryInput TO VALIDATED_NUMBER_INPUT()                          [FR7, FR9]
Line 15:    SET risePercentage TO VALIDATED_NUMBER_INPUT()                              [FR7, FR9]
Line 16:    SET matches TO FilterEmployees(employeeArray, departmentInput, minimumSalaryInput) [FR12]
Line 17:    DISPLAY formatted matches                                                    [FR7]
Line 18:    FOR EACH employee IN matches DO
Line 19:        SET newSalary TO employee.get_salary() * multiplier
Line 20:        employee.set_salary(newSalary)                                           [FR1]
Line 21:    ENDFOR
Line 22:    DISPLAY formatted updated matches                                            [FR7, FR11]
Line 23:    CLOSE conn                                                                   [FR15]
Line 24: ENDFUNCTION
```

The Python implementation is in [Program 24 - Complete OO Program.py](./Program%2024%20-%20Complete%20OO%20Program.py).

### Notes

- The program intentionally does not use `ORDER BY`; sorting is completed in Python using insertion sort.
- Getter methods are used for comparisons, filtering, and display.
- Setter methods are used for controlled updates and validation.

---

## Test plan

### Test Cases

| # | Functional Requirement | Test Description | Input / Conditions | Expected Output | Evidence |
|---|------------------------|------------------|--------------------|-----------------|----------|
| 1 | FR8 | Missing environment variable | Remove `DB_NAME` | Config error shown; program exits | Before: environment missing variable. After: error message shown. |
| 2 | FR6 | Database read works | Valid credentials | Rows fetched from Employees table | Before: DB accessible. After: records loaded message/output. |
| 3 | FR1/FR2 | Object creation uses encapsulation | Valid row data | Employee objects created using setters | Before: row sample. After: object display output. |
| 4 | FR3/FR4 | Insertion sort order is correct | Mixed salaries | Output sorted highest salary first | Before: unsorted salary set. After: sorted order verified. |
| 5 | FR9 | Numeric validation blocks invalid salary input | Enter `abc` then `-5` then `900` | Error/re-prompt until valid number | Before: invalid entries. After: accepted numeric input. |
| 6 | FR10 | Text validation blocks blank department input | Enter blank value | Error/re-prompt until non-empty value | Before: blank input. After: accepted text input. |
| 7 | FR12 | Filter logic returns matching records only | Department=`Sales`, Minimum Salary=`1000` | Only matching employees displayed | Before: known records. After: filtered output verified. |
| 8 | FR1 | Setter update applied to matched objects | Pay rise `10` | Displayed salary values increase by 10% | Before: pre-rise values. After: updated values. |
| 9 | FR11 | User feedback is clear | Normal run and no-match run | Clear progress and outcome messages | Before: run scenario. After: expected messages shown. |
| 10 | FR13/FR14 | Runtime safety | Inject invalid row data or conversion issue | Error context displayed; program continues safely | Before: fault setup. After: stable handling output. |
| 11 | FR15 | Resource cleanup always occurs | Success and early-return paths | Connection closed message shown | Before: active connection. After: safe closure confirmed. |
