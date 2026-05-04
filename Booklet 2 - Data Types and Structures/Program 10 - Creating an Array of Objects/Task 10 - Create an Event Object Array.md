# Task 10 - Create an Event Object Array

## Objective

Create an `Event` class and store event objects in a fixed-size array.

---

## Context

You have an empty Python file: `Task 10 - Create an Event Object Array.py`.

Build a program that:

1. Defines an `Event` class.
2. Uses a fixed-size array of `Event` objects.
3. Adds sample events.
4. Adds participant names to one event.
5. Displays stored data.

---

## Requirements

### Class and Properties

Create class `Event` with:
- `startDate` (string)
- `startTime` (string)
- `venue` (string)
- `reminder` (boolean)
- `participants` fixed-size array of length 20
- `index` integer to track participant insertion

### Fixed-Size Arrays (Required)

- Use `eventArray = [""] * 20` for the main event structure.
- Use `self.participants = [""] * 20` inside each `Event` object.
- Keep insertion controlled by index values.

### Methods

Implement:
- `updateDate(eventDate)`
- `getDate()`
- `addParticipant(name)`

### Output

- Create at least 2 events in the fixed-size array.
- Add at least 1 participant.
- Print participants from one event.

---

## Implementation Hints

```python
eventArray = [""] * 20
eventArray[0] = Event("14/04/2022", "0900", "Main Office", True)
eventArray[1] = Event("15/04/2022", "1030", "Staff Room", True)

eventArray[1].addParticipant("Erica Knowles")
print(eventArray[1].participants)
```

---

## Functional Requirements Covered

- Fixed-size array of objects
- Object instantiation and indexed storage
- Class methods operating on object state
- Controlled insertion into fixed-size participant list
