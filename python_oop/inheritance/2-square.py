#!/usr/bin/env python3
"""This module defines a Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a special Rectangle."""

    def __init__(self, size):
        """Initialize a square using the size for both width and height."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        rect_str = super().__str__()
        return rect_str.replace("[Rectangle]", "[Square]")
