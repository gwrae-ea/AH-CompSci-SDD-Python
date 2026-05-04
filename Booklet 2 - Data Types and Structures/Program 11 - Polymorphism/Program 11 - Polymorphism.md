# Program 11 - Polymorphism

### Technical Explanation

This program demonstrates inheritance and polymorphism using `Event` as a parent class and `WorkMeeting` and `Personal` as child classes. A fixed-size array stores mixed object types, then shared method calls show polymorphic behavior. `WorkMeeting` overrides `getDate()`, so the same method call gives different output depending on object type.

---

## Analysis

### End User Requirements

1. The user wants one structure to hold different event subtypes.
2. The user wants shared methods to work across all event objects.
3. The user wants overridden methods to return subtype-specific output.
4. The user wants clear evidence of inherited and subtype-only behavior.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Use inheritance with a parent class and at least two child classes.

FR2 Use polymorphism by calling the same method on different object types.

FR3 Override at least one parent method in a child class.

FR4 Demonstrate inherited method use from the parent class.

#### Integration

The solution is required to:

FR5 Store mixed object types in one fixed-size array.

FR6 Iterate through the array and call common methods.

FR7 Output results that prove polymorphic behavior.

#### Additional functional requirements

The solution is required to:

FR8 Use runtime checks before calling subtype-only methods.

FR9 Provide clear output labels for each test section.

FR10 Keep object creation and array population explicit.

---

## Design

### Data Structure Design

- Fixed-size array of objects: `events = [""] * 3`
- Index 0 stores `Event`, index 1 stores `WorkMeeting`, index 2 stores `Personal`.

### English Pseudocode

1. Define parent class `Event`.
2. Define child classes `WorkMeeting` and `Personal`.
3. Override `getDate()` in `WorkMeeting`.
4. Create fixed-size array of length 3.
5. Store one object of each class by index.
6. Loop through fixed-size array and call `getDate()`.
7. Safely call subtype-only methods where applicable.

---

## Implementation

[Program 11 – Polymorphism.py](./Program%2011%20%E2%80%93%20Polymorphism.py)

SQA-RL:
```text
DECLARE events : ARRAY[1:3] OF Event
SET events[1] <- NEW Event(...)
SET events[2] <- NEW WorkMeeting(...)
SET events[3] <- NEW Personal(...)

FOR eachEvent FROM 1 TO 3
    OUTPUT events[eachEvent].getDate()
    CALL events[eachEvent].addParticipant("Alice")
NEXT eachEvent
```

### Notes

- Fixed-size array is used for predictable polymorphic testing.
- Overridden methods are visible through uniform method calls.

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Create fixed mixed array | 3 objects of different types | Array holds all 3 objects | Before: empty / After: populated |
| Polymorphic call | `obj.getDate()` in loop | Type-appropriate date string | Before: same output / After: varied output |
| Inherited method call | `addParticipant("Alice")` | Participant inserted for each object | Before: empty first slot / After: `Alice` |
| Override check | `WorkMeeting.getDate()` | Returns overridden text format | Before: parent style / After: child style |
| Subtype-only method guard | call with type check | No invalid method crash | Before: runtime error / After: safe call |
