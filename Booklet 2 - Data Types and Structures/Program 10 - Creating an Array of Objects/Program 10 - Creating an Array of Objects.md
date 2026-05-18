# Program 10 - Creating an Array of Objects

### Technical Explanation

This program demonstrates how to create a developer-defined class and store multiple object instances in a fixed-size array. The `Event` class models one event, then a fixed-size array is created to hold up to 20 `Event` objects. This shows object-oriented design, indexed storage, and controlled data capacity. A participant list is also stored as a fixed-size array inside each object.

---

## Analysis

### End User Requirements

1. The user wants to store multiple events in one program structure.
2. The user wants each event to keep its own properties and participant list.
3. The user wants a fixed maximum number of events to avoid uncontrolled growth.
4. The user wants to add and view event data by index using getter methods.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Have an object-oriented solution with a developer defined class to represent event data.

FR2 Use a fixed-size array of objects to store event records.

FR3 Use indexed access to retrieve and update individual objects.

FR4 Use class methods to update and return event properties.

#### Integration

The solution is required to:

FR5 Create and populate event objects with valid sample data.

FR6 Store objects in a fixed-size array structure for processing.

FR7 Display selected object data as output.

#### Additional functional requirements

The solution is required to:

FR8 Include a fixed-size participant array in each event object.

FR9 Prevent participant insertion beyond participant array bounds.

FR10 Use clear variable names and comments for readability.

---

## Design

### Data Structure Design

- Fixed-size event array: `eventArray = [""] * 20`
- Fixed-size participant array inside each `Event`: `participants = [""] * 20`
- Integer index tracks next insertion point for participants.

### English Pseudocode

1. Define class `Event` with date, time, venue, reminder.
2. In constructor, create fixed-size participant array of length 20.
3. Create fixed-size `eventArray` of length 20.
4. Store `Event` objects in specific array positions.
5. Add a participant to one event.
6. Display participant array contents.

---

## Implementation

[Program 10 – Creating an Array of Objects.py](./Program%2010%20%E2%80%93%20Creating%20an%20Array%20of%20Objects.py)

SQA-RL:
```text
CLASS Event
    DECLARE startDate : STRING
    DECLARE startTime : STRING
    DECLARE venue : STRING
    DECLARE reminder : BOOLEAN
    DECLARE participants : ARRAY[1:20] OF STRING
    DECLARE index : INTEGER
END CLASS

DECLARE eventArray : ARRAY[1:20] OF Event
SET eventArray[1] <- NEW Event(...)
SET eventArray[2] <- NEW Event(...)
CALL eventArray[2].addParticipant("Erica Knowles")
OUTPUT eventArray[2].getParticipants()
```

### Notes

- The design and implementation both use fixed-size arrays.
- Using fixed capacity supports predictable memory and index control.

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Create fixed event array | `eventArray = [""] * 20` | Array length is 20 | Before: no array / After: length 20 |
| Insert event object | `eventArray[0] = Event(...)` | Object stored at index 0 | Before: empty / After: Event object |
| Add participant | `addParticipant("Erica")` | Participant saved at next index | Before: blank entry / After: `Erica` |
| Retrieve event property | `eventArray[1].getVenue()` | Correct venue displayed | Before: none / After: expected venue |
| Participant array bound | Add up to 20 names | No out-of-range insertion | Before: potential overflow / After: controlled capacity |
