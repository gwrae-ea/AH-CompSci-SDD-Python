# Program 17 - Binary Search on 1D Array

### Technical Explanation

This program combines sorting and searching. The array is sorted first, then Binary Search is used to locate a target value. Binary Search works by repeatedly halving the search region using low, high, and mid indices, making it much faster than linear search on sorted data.

---

## Analysis

### End User Requirements

1. The user wants to find a value quickly in a numeric dataset.
2. The user wants the array sorted before searching.
3. The user wants the index of the found value.
4. The user wants a clear "not found" result when absent.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Sort the input array before searching.

FR2 Implement Binary Search on a sorted 1D array.

FR3 Use low/high/mid indices correctly.

FR4 Return found index or `-1` when not found.

#### Integration

The solution is required to:

FR5 Read a target value from user input.

FR6 Display sorted array for verification.

FR7 Output search result clearly.

#### Additional functional requirements

The solution is required to:

FR8 Keep sorting and searching as separate functions.

FR9 Ensure search loop terminates correctly.

FR10 Handle values not present in array.

---

## Design

### Data Structure Design

- Use one 1D numeric array.
- Sort first, then search.
- Binary search region controlled by `low` and `high`.

### English Pseudocode

1. Sort numeric array ascending.
2. Set `low = 0`, `high = len(array)-1`.
3. While not found and `low <= high`:
   - Set `mid = (low + high) // 2`.
   - If target equals middle value, return `mid`.
   - If target larger, set `low = mid + 1`.
   - Else set `high = mid - 1`.
4. Return `-1` if search ends with no match.

---

## Implementation

[Program 17 – Binary Search on 1D Array.py](./Program%2017%20%E2%80%93%20Binary%20Search%20on%201D%20Array.py)

SQA-RL:
```text
FUNCTION binarySearch(numArray, target)
    SET low <- 1
    SET high <- SIZE(numArray)

    WHILE low <= high
        SET mid <- FLOOR((low + high) / 2)
        IF target = numArray[mid] THEN
            RETURN mid
        ELSE IF target > numArray[mid] THEN
            SET low <- mid + 1
        ELSE
            SET high <- mid - 1
        END IF
    END WHILE

    RETURN -1
END FUNCTION
```

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Value exists | Sorted array, target present | Valid index returned | Before: unknown / After: index >= 0 |
| Value absent | Sorted array, target missing | `-1` returned | Before: unknown / After: -1 |
| First element | target = min value | First index returned | Before: not verified / After: first index |
| Last element | target = max value | Last index returned | Before: not verified / After: last index |
| Duplicate values | target repeated | Any valid matching index | Before: uncertain / After: index with target |
