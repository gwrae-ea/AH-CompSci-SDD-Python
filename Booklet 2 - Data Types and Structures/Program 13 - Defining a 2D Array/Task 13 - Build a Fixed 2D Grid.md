# Task 13 - Build a Fixed 2D Grid

## Objective

Create and display a fixed-size 2D array grid, then place values at specific coordinates.

---

## Context

You have an empty Python file: `Task 13 - Build a Fixed 2D Grid.py`.

Build a program that:

1. Defines constants for rows and columns.
2. Creates a fixed-size 2D array initialized with blanks.
3. Places symbols at specific coordinates.
4. Displays the final grid.

---

## Requirements

### Fixed-Size 2D Array (Required)

Use a fixed-size structure, for example:

```python
ROWS, COLS = 6, 9
game = [[" " for _ in range(COLS)] for _ in range(ROWS)]
```

### Coordinate Updates

- Set at least 3 cells with symbols (for example `P` and `E`).
- Use valid row/column index values only.

### Display

- Print the grid clearly using loops or a table format.
- Include row/column labels if possible.

---

## Functional Requirements Covered

- Fixed-size 2D array definition
- Indexed coordinate updates
- Structured display of grid data
- Safe bounded access
