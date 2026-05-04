# Program 3 - Creating Methods in a Class

### Technical Explanation

This program demonstrates how to add methods (functions) to a class definition. While properties store data, methods define the behaviors and operations that objects can perform. Methods are functions defined within a class that typically operate on the object's properties. This program shows creating methods that access properties, calculate values, perform operations, and return results. Key technical skills include method definition syntax, the `self` parameter for accessing object properties, parameter passing to methods, return values, and understanding the difference between data (properties) and behavior (methods) in object-oriented programming.

---

## Analysis

### End User Requirements

1. The user wants objects to perform actions beyond just storing data (e.g., calculate salary increases, generate reports).
2. The user wants methods that operate on object properties in meaningful ways.
3. The user wants clear method names describing what action they perform.
4. The user wants methods to return useful results or modify object state appropriately.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Define methods within a class to represent object behaviors.

FR2 Use the `self` parameter to access object properties within methods.

FR3 Create methods that accept parameters to customize their behavior.

FR4 Implement methods that return values or perform state changes.

#### Integration

The solution is required to:

FR5 Demonstrate methods that retrieve or display object information.

FR6 Show methods that calculate derived values from properties.

FR7 Display clear output showing method results.

#### Additional functional requirements

The solution is required to:

FR8 Include docstrings explaining method behavior and parameters.

FR9 Implement validation or processing logic within methods.

FR10 Show method calls through consistent naming conventions.

---

## Design

### Method Structure

```
CLASS ClassName
    ...properties...
    
    METHOD MethodName(param1, param2)
        ... method implementation ...
        RETURN result
    END METHOD
END CLASS
```

---

## Implementation

[Program 3 - creating methods in a class.py](./Program%203%20%E2%80%93%20creating%20methods%20in%20a%20class.py)

### Notes

- Methods are defined with `def method_name(self, parameters):`
- Access properties using `self.property_name`
- Call methods using `object.method_name(arguments)`
- Methods can modify object properties or return values

---

## Test plan

| Test Case | Input | Expected Output | Evidence |
|-----------|-------|-----------------|----------|
| Method definition | Define method in class | Method accessible on instances | Before: AttributeError / After: Method callable |
| Method with property access | Call method that reads properties | Method accesses and uses properties correctly | Before: None / After: Properties accessed |
| Method with parameters | Call method with parameters | Parameters received and used in computation | Before: TypeError / After: Parameters processed |
| Method return value | Call method and capture return | Correct value returned | Before: None returned / After: Expected value |
| Multiple method calls | Call different methods on same object | All methods execute correctly | Before: Methods fail / After: All succeed |

