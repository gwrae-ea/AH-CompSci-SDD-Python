# Program 13 - Defining a 2D Array

### Technical Explanation

This program demonstrates how to define and use a fixed-size 2D array (rows and columns) to represent a grid. Specific coordinates are updated and the grid is displayed. This models board layouts and map-like structures where dimensions are known in advance.

---

## Analysis

### End User Requirements

1. The user wants a grid with fixed dimensions.
2. The user wants to place values at exact row/column coordinates.
3. The user wants to display the full grid clearly.
4. The user wants predictable indexing with fixed bounds.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Define a fixed-size 2D array with set row and column counts.

FR2 Use nested loops or comprehensions to initialize the full structure.

FR3 Update specific cells by row/column index.

FR4 Traverse and display the grid structure.

#### Integration

The solution is required to:

FR5 Use row and column headers for readable display.

FR6 Maintain consistent index mapping between logic and output.

FR7 Print the 2D array in a tabular format.

#### Additional functional requirements

The solution is required to:

FR8 Keep grid dimensions as constants.

FR9 Avoid out-of-range coordinate updates.

FR10 Use meaningful symbols for stored values.

---

## Design

### Data Structure Design

- Fixed-size dimensions: `ROWS = 6`, `COLS = 9`
- Fixed-size 2D array: `game = [[" " for c in range(COLS)] for r in range(ROWS)]`

### English Pseudocode

1. Set fixed row and column values.
2. Create fixed-size 2D array with blanks.
3. Set values at specific coordinates.
4. Build row/column headers.
5. Output grid in table form.

---

## Implementation

[Program 13 - Defining a 2D Array.py](./Program%2013%20-%20Defining%20a%202D%20Array.py)

SQA-RL:
```text
DECLARE ROWS <- 6
DECLARE COLS <- 9
DECLARE game : ARRAY[1:ROWS, 1:COLS] OF STRING

FOR r FROM 1 TO ROWS
    FOR c FROM 1 TO COLS
        SET game[r,c] <- " "
    NEXT c
NEXT r

SET game[3,7] <- "P"
SET game[2,3] <- "E"
SET game[5,2] <- "E"
OUTPUT game
```

### Notes

- The design and implementation explicitly use a fixed-size 2D array.
- This structure is appropriate when dimensions are known before runtime.

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Create fixed 2D array | ROWS=6, COLS=9 | 6x9 grid created | Before: no grid / After: 6x9 structure |
| Set coordinate value | `game[3][7] = "P"` | Cell contains `P` | Before: blank / After: `P` |
| Multiple placements | 3 updates | All target cells updated | Before: blanks / After: correct symbols |
| Display grid | print/table output | Readable rows and columns | Before: unclear / After: structured table |
| Bounds safety | valid indices only | No index errors | Before: risk / After: safe access |
