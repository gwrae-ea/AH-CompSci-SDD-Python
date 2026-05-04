# Task 14 - Cinema 2D Object Array

## Objective

Create a cinema booking model using a fixed-size 2D array of `Seat` objects.

---

## Context

You have an empty Python file: `Task 14 - Cinema 2D Object Array.py`.

Build a program that:

1. Defines a `Seat` class.
2. Builds a fixed-size 2D array of `Seat` objects.
3. Books seats by row/seat index.
4. Displays seating status.
5. Reports available seats and revenue.

---

## Requirements

### Seat Class

Include:
- row
- seat number
- status (`available` or `booked`)
- price

Methods:
- `book()`
- `is_available()`
- `__str__()`

### Fixed-Size 2D Array (Required)

Use constants and create a fixed-size grid:

```python
ROWS = 4
SEATS_PER_ROW = 6
cinema = [[Seat(r, s) for s in range(SEATS_PER_ROW)] for r in range(ROWS)]
```

### Booking Logic

- Implement `book_seat(cinema, row, seat_num)`.
- Prevent double booking.

### Reports

- `count_available(cinema)` traverses whole fixed-size 2D array.
- `revenue_report(cinema)` sums prices for booked seats.

### Display

- Print seating plan before and after bookings.
- Print available seats and revenue.

---

## Functional Requirements Covered

- Class-based record/object modeling
- Fixed-size 2D array of objects
- Indexed updates and full traversal
- Reporting from fixed-size grid state
