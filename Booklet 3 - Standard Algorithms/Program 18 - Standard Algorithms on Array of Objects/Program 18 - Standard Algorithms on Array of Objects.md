# Program 18 - Standard Algorithms on Array of Objects

### Technical Explanation

This program applies standard algorithms to an array of objects. Car records are read from CSV into `Car` objects, then sorted by make using Bubble Sort, and searched using Binary Search. This demonstrates how algorithm logic can be adapted from primitive values to object data accessed via getter methods.

---

## Analysis

### End User Requirements

1. The user wants car records loaded from file into object form.
2. The user wants records sorted by make.
3. The user wants to search quickly for a car make.
4. The user wants a clear available/not available result.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Define a class for car records.

FR2 Store records in an array of objects.

FR3 Sort object array by a selected field using a class getter method.

FR4 Search sorted object array using Binary Search.

#### Integration

The solution is required to:

FR5 Read external CSV data and convert rows to objects.

FR6 Output unsorted and sorted make lists.

FR7 Return and display search outcome.

#### Additional functional requirements

The solution is required to:

FR8 Keep read, sort, and search as separate functions.

FR9 Compare object properties consistently.

FR10 Handle not-found case robustly.

---

## Design

### Data Structure Design

- Use a fixed-size object array sized from CSV row count.
- Store `Car` objects by index.
- Sort/search operate on `get_car_make()`.

### English Pseudocode

1. Read all CSV lines.
2. Create fixed-size car array with length equal to lines.
3. For each row, create `Car` object and insert by index.
4. Bubble sort array by `get_car_make()`.
5. Binary search sorted array for user target make using `get_car_make()`.
6. Output found/not found message.

---

## Implementation

[Program 18 - Standard Algorithms on Array of Objects.py](./Program%2018%20-%20Standard%20Algorithms%20on%20Array%20of%20Objects.py)

SQA-RL:
```text
DECLARE carArray : ARRAY[1:n] OF Car
FOR i FROM 1 TO n
    SET carArray[i] <- NEW Car(...)
NEXT i

CALL bubbleSortArrayOfObjects(carArray) USING car_make
SET position <- binarySearch(carArray, targetMake) USING car_make

IF position = -1 THEN
    OUTPUT "Not found"
ELSE
    OUTPUT "Found"
END IF
```

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| CSV load | `carData.csv` | Array of `Car` objects populated | Before: empty / After: objects loaded |
| Sort by make | Unsorted object array | Makes in ascending order | Before: unsorted / After: sorted |
| Search existing make | target in sorted array | Found index != -1 | Before: unknown / After: found |
| Search missing make | target not in array | -1 and not-available message | Before: unknown / After: not found |
| Case sensitivity check | mixed input casing | Documented behavior (exact/normalized) | Before: unclear / After: defined behavior |
