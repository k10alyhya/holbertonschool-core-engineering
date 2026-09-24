#!/usr/bin/env python3
"""This module defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.position = position

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Return the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        for item in value:
            if not isinstance(item, int) or item < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                )

        self.__position = value

    def my_print(self):
        """Print the square."""
        print(self)

    def __str__(self):
        """Return the string representation of the square."""
        if self.__size == 0:
            return ""

        result = ""

        for i in range(self.__position[1]):
            result += "\n"

        for i in range(self.__size):
            result += (" " * self.__position[0]) + (
                "#" * self.__size
            )

            if i < self.__size - 1:
                result += "\n"

        return result
