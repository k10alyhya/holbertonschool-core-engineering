# Python - Core Data Structures

This project focuses on Python's core data structures: lists, tuples, sets, and dictionaries.

## Learning Objectives

- Iterate through lists and print elements.
- Access list elements safely.
- Replace elements in a list.
- Work with nested lists and matrices.
- Use tuples and return multiple values.
- Find common elements between sets.
- Add or update key-value pairs in dictionaries.
- Find the key with the highest value in a dictionary.

## Core Concepts

### Lists
Ordered and mutable collections.

```python
numbers = [1, 2, 3]
numbers[0] = 10
List elements can be accessed using indexes:

players[0]
players[1]

Lists are mutable, which means their elements can be changed after creation:

players[0] = "Khaled"

Common list methods include:

append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()

Example:

numbers = [1, 2, 3]
numbers.append(4)

Result:

[1, 2, 3, 4]
Indexing

Python sequences use zero-based indexing.

Example:

numbers = [10, 20, 30]

Indexes:

Index:   0   1   2
Value:  10  20  30

Example:

numbers[0]

returns:

10

Accessing an index outside the valid range may raise:

IndexError
Nested Lists

Lists can contain other lists.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

A value can be accessed using more than one index:

matrix[0][1]

returns:

2
Tuples

A tuple is a sequence of values.

Example:

player = ("Khaled", 10, "Midfielder")

Tuples support indexing:

player[0]

However, tuples are immutable.

This means that after a tuple is created, its individual elements cannot be reassigned.

Example:

player[0] = "Ali"

will raise an error.

Tuple Packing and Unpacking

Multiple values can be packed into a tuple:

player = "Khaled", 10, "Midfielder"

They can also be unpacked into variables:

name, number, position = player

The number of variables must match the number of values.

Sets

A set is an unordered collection with no duplicate elements.

Example:

teams = {"Al Hilal", "Al Nassr", "Al Hilal"}

Duplicate values are removed.

Sets are useful for:

Removing duplicates.
Membership testing.
Mathematical set operations.

Example:

"Al Hilal" in teams

Set operations include:

a | b

Union

a & b

Intersection

a - b

Difference

a ^ b

Symmetric difference

An empty set must be created using:

set()

because:

{}

creates an empty dictionary.

Dictionaries

A dictionary stores data as key-value pairs.

Example:

goals = {
    "Player A": 10,
    "Player B": 7,
    "Player C": 12
}

Values are accessed using keys:

goals["Player A"]

returns:

10

Dictionary keys must be unique.

A dictionary can be updated:

goals["Player A"] = 11

A new key-value pair can also be added:

goals["Player D"] = 5
List vs Tuple vs Set vs Dictionary
Type	Ordered	Mutable	Duplicates	Access
List	Yes	Yes	Yes	Index
Tuple	Yes	No	Yes	Index
Set	No	Yes	No	Membership
Dictionary	Key-value mapping	Yes	Keys must be unique	Key
Project Concepts

This project includes practice with:

Iterating through lists.
Accessing elements safely.
Replacing list elements.
Working with matrices.
Adding tuples.
Finding common elements between sets.
Updating dictionaries.
Finding values inside dictionaries.
Resources
Python Tutorial - Data Structures
Python Tutorial - Sets
Python Tutorial - Dictionaries
Python Built-in Types

Official documentation:
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/tutorial/datastructures.html#sets
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
https://docs.python.org/3/library/stdtypes.html
