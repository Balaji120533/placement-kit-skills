# OOP — facts

## Four pillars
- **Encapsulation:** bundle data and methods, hide state behind access control.
- **Abstraction:** expose what an object does, hide how.
- **Inheritance:** a class reuses and extends another (is-a).
- **Polymorphism:** one interface, many behaviours.

## Overloading vs overriding
| | Overloading | Overriding |
| --- | --- | --- |
| Binding | Compile time (static) | Run time (dynamic) |
| Signature | Same name, different parameters | Same name and parameters in subclass |
| Return type alone | Cannot distinguish overloads | Must be same or covariant |
| Where | Same class (or inherited) | Parent–child classes |

Java: `static`, `private` and `final` methods are not overridden (static is hidden).

## Abstract class vs interface (Java)
| | Abstract class | Interface |
| --- | --- | --- |
| Instantiate | No | No |
| Multiple inheritance | A class extends only one | A class can implement many |
| State | Can have instance fields | Only constants (`public static final`) |
| Methods | Abstract and concrete | Abstract, plus default/static methods (Java 8+) |
| Constructors | Yes | No |

## Other
- Constructor: same name as the class, no return type, called at object creation. Java has no destructor (garbage collection).
- `this` refers to the current object; `super` to the parent.
- Static members belong to the class, not an instance.
- C++: a virtual function enables runtime polymorphism; a pure virtual (`= 0`) makes the class abstract. Java does not support multiple inheritance of classes; C++ does.

## Common MCQ traps
- "Overloading is runtime polymorphism" is false.
- Private members are not inherited for access, though they exist in the object.
- An abstract class can have a constructor and non-abstract methods.
- Say which language the question assumes when behaviour differs (Java vs C++).
