# Task 12 - CSV to Fixed Object Array

## Objective

Use Program 12 (Event example) as a pattern, then write your own version that reads vehicle data from CSV and stores rows as `Vehicle` objects in a fixed-size array.

---

## Context

You have an empty Python file: `Task 12 - CSV to Fixed Object Array.py`.

Program 12 is the worked example using `Event` objects.

Your task is to create a *new adapted version* that:

1. Defines a `Vehicle` class.
2. Reads `dataFiles/vehicleData.csv`.
3. Creates a fixed-size object array based on data-row count.
4. Converts each CSV data row to a `Vehicle` object by index.
5. Prints selected object properties.

---

## Requirements

### CSV File to Use

Use `dataFiles/vehicleData.csv` for the student task.

Reference only: Program 12 uses `eventData.csv` as the example implementation.

This file has a header row:

`numWheels,colour,fuel,seats,roof,maxVel`

### Class Requirements

Create your own `Vehicle` class (adapting the Program 12 Event approach) with these properties:

- `numWheels`
- `colour`
- `fuel`
- `seats`
- `roof`
- `maxVel`

### Fixed-Size Array Requirement

Do not use unbounded growth as final storage.

Use fixed-size allocation based on data rows (excluding header):

```python
lines = open("dataFiles/vehicleData.csv").read().splitlines()
data_lines = lines[1:]  # skip header
vehicleArray = [""] * len(data_lines)
```

Then populate by index in a loop.

### Parsing Requirements

- Skip the first CSV row because it is the header.
- Split each data line by comma.
- Map each field to `Vehicle` constructor parameters in order.
- Keep conversion order consistent.

### Output Requirements

- Print at least 2 values from stored objects by index.
- Example: first vehicle colour and another vehicle max velocity.

---

## Functional Requirements Covered

- Adaptation of a worked example (`Event`) into a new class/data context (`Vehicle`)
- File input and CSV parsing
- Object creation from row data
- Fixed-size array allocation and indexed insertion
- Indexed retrieval and display
