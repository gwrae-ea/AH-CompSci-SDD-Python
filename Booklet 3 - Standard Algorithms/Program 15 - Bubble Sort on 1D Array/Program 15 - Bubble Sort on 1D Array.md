# Program 15 - Bubble Sort on 1D Array

### Technical Explanation

This program demonstrates Bubble Sort on a 1D array of numbers. Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order, so larger values move toward the end of the array each pass. The implementation also uses a `swapped` flag to stop early if the list is already sorted.

---

## Analysis

### End User Requirements

1. The user wants numeric data sorted into ascending order.
2. The user wants to see the array before and after sorting.
3. The user wants a clear, repeatable algorithm.
4. The user wants sorting to stop when no more swaps are needed.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Use a 1D array to store the numeric dataset.

FR2 Implement Bubble Sort using adjacent comparisons.

FR3 Swap out-of-order values correctly.

FR4 Return the sorted array.

#### Integration

The solution is required to:

FR5 Display array contents before sorting.

FR6 Display array contents after sorting.

FR7 Use a loop control mechanism to stop when sorted.

#### Additional functional requirements

The solution is required to:

FR8 Reduce pass length each iteration.

FR9 Avoid unnecessary passes when no swaps occur.

FR10 Keep the function reusable for different input arrays.

---

## Design

### Data Structure Design

- Use a 1D numeric array.
- Track active unsorted region with variable `n`.
- Use boolean `swapped` for early stop.

### English Pseudocode

1. Set `n` to array length.
2. Set `swapped` to true.
3. While `swapped` is true and `n` is valid:
   - Set `swapped` false.
   - Loop from index 0 to `n-2`.
   - Compare adjacent values.
   - Swap when left value is larger.
   - Set `swapped` true if a swap occurs.
4. Decrease `n` after each pass.
5. Return sorted array.

---

## Implementation

[Program 15 – Bubble Sort on 1D Array.py](./Program%2015%20%E2%80%93%20Bubble%20Sort%20on%201D%20Array.py)

SQA-RL:
```text
FUNCTION bubbleSort(numArray)
    SET n <- SIZE(numArray)
    SET swapped <- TRUE

    WHILE swapped = TRUE AND n >= 0
        SET swapped <- FALSE
        FOR i <- 1 TO n-1
            IF numArray[i] > numArray[i+1] THEN
                SWAP numArray[i], numArray[i+1]
                SET swapped <- TRUE
            END IF
        NEXT i
        SET n <- n - 1
    END WHILE

    RETURN numArray
END FUNCTION
```

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Unsorted list | `[23, 546, 2, 3214]` | `[2, 23, 546, 3214]` | Before: unsorted / After: sorted ascending |
| Already sorted | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` with minimal passes | Before: sorted / After: unchanged |
| Reverse order | `[9, 7, 5, 3]` | `[3, 5, 7, 9]` | Before: descending / After: ascending |
| Duplicate values | `[4, 2, 4, 1]` | `[1, 2, 4, 4]` | Before: mixed / After: duplicates retained |
| Single item | `[10]` | `[10]` | Before: one element / After: unchanged |
