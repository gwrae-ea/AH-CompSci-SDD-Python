# Task 18 - Sort and Search an Object Array

## Objective

Use a worked example to build a program that reads CSV into object records, sorts by one property, and performs Binary Search on the sorted object array.

---

## Context

You have an empty Python file: `Task 18 - Sort and Search an Object Array.py`.

Use Program 18 as the example pattern.

---

## Requirements

1. Create a class to represent one row of car data.
2. Read CSV rows and create objects.
3. Store objects in an array.
4. Sort array by `car_make` using Bubble Sort.
5. Search sorted object array using Binary Search.
6. Ask user for target make and display found/not found.

### Preferred Array Structure

Use a fixed-size object array based on CSV row count:

```python
lines = open("dataFiles/carData.csv").read().splitlines()
carArray = [""] * len(lines)
```

Then populate by index.

---

## Suggested Tests

- Existing make in file
- Missing make in file
- First and last make after sorting
- Duplicate make values
- Input normalization choice (exact or lowercased)

---

## Functional Requirements Covered

- Array-of-objects processing
- Bubble Sort using object property
- Binary Search using object property
- User-driven search output
