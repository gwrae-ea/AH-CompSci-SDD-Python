# Program 14 - 2D Array of Records or Objects

### Technical Explanation

This program models cinema seating with a class (`Seat`) and a fixed-size 2D array of objects. Each grid position stores one `Seat` object containing row, seat number, booking status, and price. The design demonstrates class-based records, fixed-size 2D array population, traversal, and reporting operations.

---

## Analysis

### End User Requirements

1. The user wants a seating grid with a fixed number of rows and seats.
2. The user wants each seat to store its own state and price.
3. The user wants to book seats by row and seat index.
4. The user wants to see available seats and current revenue.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Use a class to represent a seat record/object.

FR2 Use a fixed-size 2D array of seat objects.

FR3 Traverse the full 2D array for counting and reporting.

FR4 Update object state through class methods.

#### Integration

The solution is required to:

FR5 Create the 2D seat structure from constants.

FR6 Support booking by indexed coordinates.

FR7 Display current seating and summary information.

#### Additional functional requirements

The solution is required to:

FR8 Prevent double booking through status checks.

FR9 Produce available-seat and revenue reports.

FR10 Keep pricing rules by row.

---

## Design

### Data Structure Design

- Fixed-size dimensions: `ROWS = 4`, `SEATS_PER_ROW = 6`
- Fixed-size 2D object array:
  `cinema = [[Seat(r, s) for s in range(SEATS_PER_ROW)] for r in range(ROWS)]`

### English Pseudocode

1. Define `Seat` class with row, number, status, price.
2. Create fixed-size 2D array of `Seat` objects.
3. Book selected seats by row/column index.
4. Traverse fixed-size 2D array to count available seats.
5. Traverse fixed-size 2D array to sum booked revenue.
6. Display seating grid and reports.

---

## Implementation

[Program 14 - 2D Array of Records or Objects.py](./Program%2014%20-%202D%20Array%20of%20Records%20or%20Objects.py)

SQA-RL:
```text
DECLARE ROWS <- 4
DECLARE SEATS_PER_ROW <- 6
DECLARE cinema : ARRAY[1:ROWS, 1:SEATS_PER_ROW] OF Seat

FOR r FROM 1 TO ROWS
    FOR s FROM 1 TO SEATS_PER_ROW
        SET cinema[r,s] <- NEW Seat(r, s)
    NEXT s
NEXT r

CALL bookSeat(cinema, 1, 2)
CALL bookSeat(cinema, 2, 3)

SET availableCount <- 0
SET revenue <- 0
FOR r FROM 1 TO ROWS
    FOR s FROM 1 TO SEATS_PER_ROW
        IF cinema[r,s].isAvailable() THEN
            SET availableCount <- availableCount + 1
        ELSE
            SET revenue <- revenue + cinema[r,s].price
        END IF
    NEXT s
NEXT r
```

### Notes

- Both design and implementation use a fixed-size 2D array of objects.
- Object methods encapsulate booking and availability checks.

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Create fixed 2D cinema | ROWS=4, SEATS=6 | 24 Seat objects created | Before: none / After: full grid |
| Book valid seat | `book_seat(cinema, 0, 1)` | Seat status becomes booked | Before: available / After: booked |
| Double booking | Same seat booked twice | Second booking rejected | Before: second success / After: warning and fail |
| Count available seats | Traverse full grid | Correct available count | Before: unknown / After: exact count |
| Revenue report | Traverse booked seats | Sum of booked prices | Before: 0/wrong / After: correct revenue |
