# Student/Employee Data Model: Dataclass vs Traditional Class

## Objective
To implement an employee data model using both traditional Python classes and modern `@dataclass` structures, evaluating differences in syntax overhead, maintainability, and memory consumption.

## Algorithm
1. Create a traditional Python class with manual constructor and string representation methods.
2. Create an equivalent dataclass utilizing the `@dataclass` decorator and explicit type annotations.
3. Instantiate both models with sample record data.
4. Measure memory usage via `sys.getsizeof()`.

## Input
* Employee details: ID (`101`), Name (`"Alice Smith"`), Department (`"Cybersecurity"`), Salary (`75000.0`).

## Output
* Printed string representations and memory size comparisons for both implementations.

## Time & Space Complexity
* **Time Complexity**: $O(1)$ for object creation and attribute access.
* **Space Complexity**: $O(1)$ constant auxiliary memory per instance.
