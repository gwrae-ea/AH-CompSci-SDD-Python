# Program 2 - Instantiate and Test

### Technical Explanation

This program demonstrates how to create (instantiate) objects from a class definition and test that the objects are created correctly. Once a class template has been defined, the program shows how to call the class as a constructor to create instance objects with specific data. The program demonstrates passing parameters to the constructor, storing those values as properties in the new object, and accessing properties from an instantiated object. These skills are fundamental to using object-oriented design: defining the blueprint (class) and then creating actual working copies (instances) from that blueprint.

---

## Analysis

### End User Requirements

1. The user wants to create objects that represent specific employee records with actual data.
2. The user wants to verify that object properties are set correctly during creation.
3. The user wants to access object properties to retrieve stored data.
4. The user wants to create multiple independent objects, each with different data.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Instantiate objects from a developer-defined class.

FR2 Pass parameters to constructor to initialize object properties.

FR3 Access object properties using dot notation (object.property).

FR4 Verify that each object instance maintains independent data.

#### Integration

The solution is required to:

FR5 Import and use a class defined in another module or location.

FR6 Create and manage multiple instances without data corruption or mixing.

FR7 Display or output object data to verify correct instantiation.

#### Additional functional requirements

The solution is required to:

FR8 Demonstrate constructor parameter passing and mapping to properties.

FR9 Show accessing individual properties from created objects.

FR10 Verify property independence between different object instances.

FR11 Display clear output showing successful object creation and property values.

---

## Design

### Object Creation Pattern

```
DECLARE object1 AS NEW ClassName(param1, param2, param3, ...)
DECLARE object2 AS NEW ClassName(param1, param2, param3, ...)

CALL object1.DisplayInfo()
CALL object2.DisplayInfo()
```

---

## Implementation

[Program 2 - instantiate and test.py](./Program%202%20%E2%80%93%20instantiate%20and%20test.py)

### Notes

- Each call to the class constructor creates a new, independent object
- Properties of one object are not affected by changes to another object
- The class definition is reusable—many objects can be created from the same class

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Object instantiation | Create Employee object | Object created without error | Before: NameError / After: Object created |
| Constructor parameters passed | Create object with specific values | Object properties contain passed values | Before: Properties undefined / After: Values stored |
| Multiple independent instances | Create two Employee objects with different data | Each object has its own distinct values | Before: Data shared/overwritten / After: Independent values |
| Property access | Access object.property_name | Correct value returned from object | Before: AttributeError / After: Value retrieved |
| Object comparison | Create two instances with same data | Objects are distinct (different memory locations) | Before: Objects compared as equal / After: Distinct objects |

