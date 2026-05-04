# Program 1 - Defining a Class

### Technical Explanation

This program demonstrates the fundamental concept of object-oriented programming: creating a class definition. A class serves as a blueprint or template for creating objects that represent real-world entities. This program defines a class with properties (also called attributes or variables) that store data about an instance. Key technical skills demonstrated include class structure, properties/variables, class naming conventions, and the concept that a class definition does not create objects—it only specifies what properties each object should have.

---

## Analysis

### End User Requirements

1. The user wants to define a class structure that can represent a real-world entity.
2. The user wants the class to have appropriate properties for storing data about that entity.
3. The user wants to ensure the class definition is clear and follows standard naming conventions.
4. The user wants to verify the class has been defined correctly before using it to create objects.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Have an object-oriented solution with a developer defined class to represent <entity> data with appropriate properties.

FR2 Use appropriate property names that clearly describe what data is stored in each property.

FR3 Implement properties as instance variables with consistent naming conventions.

FR4 Include a docstring or comments explaining the purpose of the class and each property.

#### Integration

The solution is required to:

FR5 Define the class in a Python module that can be imported and reused by other programs.

FR6 Ensure the class definition follows Python naming conventions (PascalCase for class names).

FR7 Provide clear property structure that could be displayed or printed for verification.

#### Additional functional requirements

The solution is required to:

FR8 Use either an `__init__` method or property decorators to initialize class attributes.

FR9 Include property validation where appropriate (e.g., checking data types or ranges).

FR10 Provide a human-readable output method (e.g., `__str__` or `__repr__`) to display class instances.

FR11 Document the class interface clearly for other developers to understand how to use it.

---

## Design

### Class Structure

The class should define properties appropriate to the real-world entity being modeled. Properties should be:
- Named clearly (e.g., `name`, `id`, `age`, `salary`)
- Typed appropriately (string, integer, float, boolean)
- Initialized with sensible default values or passed as constructor parameters

### Example Structure

```
CLASS <EntityName>
    PROPERTY <property1>
    PROPERTY <property2>
    PROPERTY <property3>
    ...
    METHOD __init__(parameters)
        ASSIGN each parameter to corresponding property
END CLASS
```

---

## Implementation

[Program 1 - defining a class.py](./Program%201%20-%20defining%20a%20class.py)

SQA-RL (Sample structure):
```
CLASS Student
    DECLARE studentID AS INTEGER
    DECLARE firstName AS STRING
    DECLARE lastName AS STRING
    DECLARE dateOfBirth AS DATE
    DECLARE enrollmentDate AS DATE
END CLASS
```

### Notes

- The class definition creates a template but does not create any objects yet
- Each property will hold one piece of data per object instance
- The `__init__` method (if included) allows passing initial values when creating objects
- Python uses the `self` parameter to refer to instance properties

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Class can be imported | Import class in another module | No import errors | Before: ImportError / After: Import successful |
| Class has required properties | Instantiate class | All properties accessible | Before: AttributeError / After: Properties accessible |
| Properties store data correctly | Create instance with values | Values match input | Before: Values not set / After: Values stored correctly |
| Properties are independent per instance | Create two instances with different values | Each instance maintains its own values | Before: Values overwrite / After: Independent values |
| Class has appropriate output method | Print instance | Human-readable representation shown | Before: `<__main__.Class object>` / After: `Class(prop1=..., prop2=...)` |

