import numpy
import pandas

ROWS = 4
SEATS_PER_ROW = 6
ROW_PRICES = {0: 8.50, 1: 12.00, 2: 12.00, 3: 15.00}


# ── Seat Class ────────────────────────────────────────────────
class Seat:
    def __init__(self, row, seat_num):
        self.row      = int(row)
        self.seat_num = int(seat_num)
        self.status   = str("available")
        self.price    = float(ROW_PRICES[self.row])

    def book(self):
        if self.status == "booked":
            print(f"  Seat {self.row}/{self.seat_num} is already taken.")
            return False
        self.status = str("booked")
        print(f"  Booked seat {self.row}/{self.seat_num} — £{self.price:.2f}")
        return True

    def is_available(self):
        return self.status == "available"

    def __str__(self):
        return (f"R:{self.row} S:{self.seat_num}\n"
                f"£{self.price:.2f}\n"
                f"{self.status}")


# ── Cinema functions ──────────────────────────────────────────
def create_cinema(rows, seats_per_row):
    cinema = []
    for r in range(rows):
        row = []
        for s in range(seats_per_row):
            row.append(Seat(r, s))
        cinema.append(row)
    return cinema

def book_seat(cinema, row, seat_num):
    cinema[row][seat_num].book()

def display_cinema(cinema):
    grid = [[" " for s in range(SEATS_PER_ROW + 1)] for r in range(ROWS + 1)]

    for r in range(ROWS):
        for s in range(SEATS_PER_ROW):
            grid[r + 1][s + 1] = str(cinema[r][s])   # use __str__ for full details

    rowHeaders = [f"Row {r}" for r in range(ROWS)]
    colHeaders = [f"Seat {s}" for s in range(SEATS_PER_ROW)]

    dispCinema = numpy.array(grid)
    dispCinema = pandas.DataFrame(dispCinema[1:, 1:], columns=colHeaders, index=rowHeaders)
    dispCinema.columns.name = "Cinema"

    print("\n      --- SCREEN ---\n")
    print(dispCinema)
    print()

def count_available(cinema):
    count = 0
    for r in range(ROWS):
        for s in range(SEATS_PER_ROW):
            if cinema[r][s].is_available():
                count += 1
    return count

def revenue_report(cinema):
    total = 0.0
    for r in range(ROWS):
        for s in range(SEATS_PER_ROW):
            if not cinema[r][s].is_available():
                total += cinema[r][s].price
    return total


# ── Demo ──────────────────────────────────────────────────────
cinema = create_cinema(ROWS, SEATS_PER_ROW)

print("=== Initial seating plan ===")
display_cinema(cinema)

print("=== Booking seats ===")
book_seat(cinema, 0, 1)
book_seat(cinema, 1, 2)
book_seat(cinema, 2, 0)
book_seat(cinema, 3, 4)
book_seat(cinema, 0, 1)   # already booked — should fail

print("\n=== Updated seating plan ===")
display_cinema(cinema)

print(f"Available seats : {count_available(cinema)}")
print(f"Revenue so far  : £{revenue_report(cinema):.2f}")