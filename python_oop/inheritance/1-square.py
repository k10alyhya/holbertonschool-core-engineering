#!/usr/bin/env python3
"""This module defines a Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a special Rectangle."""

    def __init__(self, size):
        """Initialize a square using the size for both width and height."""
        # نتحقق من size بأنفسنا أول، عشان لو فشل التحقق تطلع
        # رسالة الخطأ بكلمة "size" (مو "width") - لأن لو تركنا
        # الأب يتحقق منها لوحده، بيعتبرها width ويغلط بالرسالة.
        self.integer_validator("size", size)
        super().__init__(size, size)
