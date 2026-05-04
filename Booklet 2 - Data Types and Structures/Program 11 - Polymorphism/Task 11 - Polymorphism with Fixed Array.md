# Task 11 - Polymorphism with Fixed Array

## Objective

Create a parent class and child classes, then demonstrate polymorphism using a fixed-size array of objects.

---

## Context

You have an empty Python file: `Task 11 - Polymorphism with Fixed Array.py`.

Build a program that:

1. Defines `Event`, `WorkMeeting`, and `Personal` classes.
2. Uses inheritance and method override.
3. Stores mixed objects in a fixed-size array.
4. Loops through the array to call shared methods.

---

## Requirements

### Class Requirements

- Parent class `Event` with common properties and methods.
- Child class `WorkMeeting` with `getDate()` override.
- Child class `Personal` with extra properties and methods.

### Fixed-Size Array Requirement

Use a fixed-size array for polymorphism testing:

```python
events = [""] * 3
events[0] = Event(...)
events[1] = WorkMeeting(...)
events[2] = Personal(...)
```

### Method Tests

- In a loop, call `getDate()` for each object.
- In the same loop, call inherited `addParticipant("Alice")`.
- Add runtime checks for subtype-only methods.

### Output

- Print clear headings for each test section.
- Show results of polymorphic calls.
- Show one subtype-specific result safely.

---

## Functional Requirements Covered

- Inheritance and method overriding
- Polymorphism with shared method calls
- Fixed-size array of mixed object types
- Safe runtime handling of subtype-only behavior
