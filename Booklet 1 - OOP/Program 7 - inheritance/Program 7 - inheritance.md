# Program 7 - Inheritance

### Technical Explanation

This program demonstrates inheritance, a fundamental OOP principle where a new class (child/derived class) inherits properties and methods from an existing class (parent/base class). Inheritance allows code reuse and establishes logical hierarchies. For example, an `Employee` class can be the parent, and a `Manager` child class inherits all Employee properties and methods while adding Manager-specific properties (e.g., `department_budget`, `team_size`) and methods (e.g., `approve_expense()`). The program demonstrates how the child class can override parent methods to customize behavior, how to call parent class methods using `super()`, and how both classes can be used interchangeably where inheritance is appropriate. Key technical skills include class hierarchies, method overriding, the `super()` function, inheritance syntax, and polymorphic behavior.

---

## Analysis

### End User Requirements

1. The user wants to model different types of employees (manager, developer, etc.) without duplicating common code.
2. The user wants specialized behavior for different employee types while reusing common base functionality.
3. The user wants the ability to treat different employee types consistently where their behavior is the same.
4. The user wants to extend the system with new employee types without modifying existing code.

### Functional Requirements

#### Advanced Higher concepts

The solution is required to:

FR1 Define a parent class with common properties and methods.

FR2 Define a child class that inherits from the parent class.

FR3 Child class inherits all parent properties and methods.

FR4 Child class can add new properties specific to its type.

#### Integration

The solution is required to:

FR5 Child class can override parent methods to provide specialized behavior.

FR6 Child class can call parent methods using `super()` when needed.

FR7 Both parent and child objects can be displayed and used polymorphically.

#### Additional functional requirements

The solution is required to:

FR8 Demonstrate inheritance syntax and class hierarchies.

FR9 Show how child classes extend parent functionality.

FR10 Display clear output showing behavior of inherited and overridden methods.

FR11 Document the inheritance relationship clearly in code.

---

## Design

### Inheritance Hierarchy

```
CLASS Employee
    PROPERTIES: id, name, salary, ...
    METHODS: get_salary(), apply_raise(), ...
END CLASS

CLASS Manager EXTENDS Employee
    ADDITIONAL PROPERTIES: team_size, budget, ...
    ADDITIONAL METHODS: approve_expense(), add_to_team(), ...
    OVERRIDE METHODS: get_info() (add manager-specific info)
END CLASS

CLASS Developer EXTENDS Employee
    ADDITIONAL PROPERTIES: programming_languages, projects, ...
    ADDITIONAL METHODS: add_language(), assign_project(), ...
END CLASS
```

---

## Implementation

[Program 7 - inheritance.py](./Program%207%20%E2%80%93%20inheritance.py)

### Notes

- Parent class is the base; child class builds on it
- Child class inherits without modification
- Child can override parent methods
- `super()` calls parent implementation

---

## Test plan

| Test Case | Operation | Expected | Evidence |
|-----------|-----------|----------|----------|
| Child inherits properties | Create child, access parent property | Property accessible | Before: AttributeError / After: Value |
| Child inherits methods | Call parent method on child object | Parent method works on child | Before: AttributeError / After: Method works |
| Child adds properties | Add property in child class | New property on child, not parent | Before: N/A / After: Property exists |
| Child adds methods | Add method in child class | New method callable on child | Before: AttributeError / After: Method works |
| Method override | Override parent method in child | Child version executes | Before: Parent version / After: Child version |
| Polymorphism | Use child where parent expected | Works due to inheritance | Before: Type error / After: Works |

