# Python - Classes & Object Model

This project is about learning the basics of Object-Oriented Programming (OOP) in Python.

The project starts by exploring existing Python objects, then moves into creating custom classes such as `Square` and `Rectangle`.

## What I Learned

- Objects, classes, and instances
- `type()`, `id()`, and `dir()`
- `self`
- `__init__`
- Instance attributes
- Private attributes
- Validation
- `@property`
- Getters and setters
- Instance methods
- `__str__`
- Basic object modeling

## Tasks and Files

| Task | File | Description |
|---|---|---|
| 0 | REPL / Quiz | Explore Python objects using `type()`, `id()`, and `dir()` |
| 1 | `1-square.py` | Create an empty `Square` class |
| 2 | `2-square.py` | Add a private size attribute |
| 3 | `3-square.py` | Add size validation |
| 4 | `4-square.py` | Add a method to calculate the square area |
| 5 | `5-square.py` | Add getter and setter using `@property` |
| 6 | `6-square.py` | Print the square using `#` |
| 7 | `7-square.py` | Add a readable string representation using `__str__` |
| 8 | `8-rectangle.py` | Create a `Rectangle` class |
| 9 | `9-rectangle.py` | Add area and perimeter methods |
| 10 | Quiz | Review the main OOP concepts |

## Main Idea

A class is used to create objects.

Each object can have its own data, called attributes, and its own behavior, defined using methods.

Example:

```python
class Player:
    def __init__(self, name):
        self.name = name


player = Player("Khaled")

Here:

- Player is the class.
- player is an instance.
- name is an instance attribute.