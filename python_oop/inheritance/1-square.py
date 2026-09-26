#!/usr/bin/env python3
"""This module defines a Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a special Rectangle."""

    def __init__(self, size):
        """Initialize a square using the size for both width and height."""
        # نستدعي __init__ حق الأب Rectangle، ونمرر له size
        # مرتين (مرة كـ width ومرة كـ height)، لأن المربع
        # هو مستطيل عرضه وطوله متساويين. الأب هو اللي يتكفل
        # بالتحقق (integer_validator) وتخزين القيم.
        super().__init__(size, size)
