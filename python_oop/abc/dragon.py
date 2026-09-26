#!/usr/bin/env python3
"""
This module contains mixin classes for swimming and flying behaviors,
and a Dragon class that inherits from both mixins.
"""


class SwimMixin:
    """Mixin providing swimming functionality."""

    def swim(self):
        """Prints swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying functionality."""

    def fly(self):
        """Prints flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that combines swimming, flying, and roaring capabilities."""

    def roar(self):
        """Prints roaring action."""
        print("The dragon roars!")
