# Program 16 - Insertion Sort on 1D Array

### Technical Explanation

This program demonstrates Insertion Sort on a 1D array. Insertion Sort builds a sorted section from left to right, taking one value at a time and inserting it into the correct position in the sorted section by shifting larger values right.

---

## Analysis

### End User Requirements

1. The user wants a reliable ascending sort on numeric data.
2. The user wants sorting performed in place on the existing array.
3. The user wants clear insertion-based algorithm logic.
4. The user wants sorted output displayed.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Use a 1D array as the main data structure.

FR2 Implement Insertion Sort using shifting and insertion.

FR3 Track current value and insertion index correctly.

FR4 Return the sorted array.

#### Integration

The solution is required to:

FR5 Process each element from index 1 onward.

FR6 Shift larger preceding values right.

FR7 Insert each value into its correct location.

#### Additional functional requirements

The solution is required to:

FR8 Keep sorting logic in a reusable function.

FR9 Preserve all original values during shifting.

FR10 Print the sorted array for verification.

---

## Design

### Data Structure Design

- Use one 1D numeric array.
- Maintain `value` (item being inserted) and `index` (current insert position).

### English Pseudocode

1. Loop `i` from 1 to end of array.
2. Set `value` to current element.
3. Set `index` to `i`.
4. While `index > 0` and previous element is larger:
   - Shift previous element right.
   - Decrease `index`.
5. Insert `value` at `index`.
6. Continue until all elements processed.

---

## Implementation

[Program 16 – Insertion Sort on 1D Array.py](./Program%2016%20%E2%80%93%20Insertion%20Sort%20on%201D%20Array.py)

SQA-RL:
```text
FUNCTION insertionSort(numArray)
    FOR i <- 2 TO SIZE(numArray)
        SET value <- numArray[i]
        SET index <- i

        WHILE index > 1 AND value < numArray[index-1]
            SET numArray[index] <- numArray[index-1]
            SET index <- index - 1
        END WHILE

        SET numArray[index] <- value
    NEXT i

    RETURN numArray
END FUNCTION
```

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Unsorted list | `[23, 546, 2, 3214]` | `[2, 23, 546, 3214]` | Before: unsorted / After: sorted ascending |
| Nearly sorted | `[1, 2, 4, 3, 5]` | `[1, 2, 3, 4, 5]` | Before: one item out / After: corrected |
| Reverse order | `[5, 4, 3, 2, 1]` | `[1, 2, 3, 4, 5]` | Before: descending / After: ascending |
| Duplicate values | `[4, 2, 4, 1]` | `[1, 2, 4, 4]` | Before: mixed / After: duplicates retained |
| Single item | `[10]` | `[10]` | Before: one element / After: unchanged |
