# Program 12 - Read from CSV to Array of Objects

### Technical Explanation

This program reads event records from a CSV file and converts each row into an `Event` object. The objects are then stored in a fixed-size array for indexed access and processing. This combines file handling, parsing, object creation, and fixed-capacity array design.

---

## Analysis

### End User Requirements

1. The user wants event data loaded from a CSV file automatically.
2. The user wants each CSV row represented as an object.
3. The user wants the resulting objects stored in a predictable fixed-size structure.
4. The user wants to access loaded events by index and getter method.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Define an `Event` class used for object instantiation from CSV rows.

FR2 Parse CSV lines into fields and map fields to object properties.

FR3 Store loaded objects in a fixed-size array.

FR4 Use indexed access to retrieve loaded object data.

#### Integration

The solution is required to:

FR5 Read an external CSV file from disk.

FR6 Convert each row to an object reliably.

FR7 Output values from selected object indices.

#### Additional functional requirements

The solution is required to:

FR8 Handle file open/read/close correctly.

FR9 Use a row counter to control fixed-size insertion.

FR10 Keep parsing logic clear and maintainable.

---

## Design

### Data Structure Design

- Read all lines from CSV first.
- Create fixed-size array: `eventArray = [""] * len(linesArray)`
- Insert one `Event` object per row by index.

### English Pseudocode

1. Open CSV file and read all lines.
2. Create fixed-size array sized to number of lines.
3. For each line:
   - Split by comma.
   - Instantiate `Event` object.
   - Store object at current index.
4. Return fixed-size object array.
5. Display selected properties.

---

## Implementation

[Program 12 - Read from CSV to Array of Objects.py](./Program%2012%20-%20Read%20from%20CSV%20to%20Array%20of%20Objects.py)

SQA-RL:
```text
OPENFILE "dataFiles/eventData.csv" FOR READ
SET linesArray <- READALLLINES
CLOSEFILE

DECLARE eventArray : ARRAY[1:SIZE(linesArray)] OF Event
SET idx <- 1
FOR eachLine IN linesArray
    SET fields <- SPLIT(eachLine, ",")
    SET eventArray[idx] <- NEW Event(fields[1], fields[2], fields[3], fields[4])
    SET idx <- idx + 1
NEXT eachLine

OUTPUT eventArray[1].getVenue()
OUTPUT eventArray[24].getStartTime()
```

### Notes

- The implementation must use a fixed-size array, not unbounded append-only storage.
- Index-based insertion keeps design aligned with AH array requirements.

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| File read | Valid CSV path | Lines loaded into memory | Before: no data / After: lines array populated |
| Fixed-size array creation | `len(linesArray)` | Array capacity equals row count | Before: no array / After: correct capacity |
| Row-to-object conversion | One CSV row | One `Event` object created | Before: raw string / After: object |
| Indexed insertion | `eventArray[idx] = Event(...)` | Objects stored in sequence | Before: blanks / After: objects |
| Output check | `eventArray[0].getVenue()` | Correct value from CSV | Before: incorrect/none / After: expected value |
