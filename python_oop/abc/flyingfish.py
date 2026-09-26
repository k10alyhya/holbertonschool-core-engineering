#!/usr/bin/env python3
"""This module defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Make the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """Describe the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Make the bird fly."""
        print("The bird is flying")

    def habitat(self):
        """Describe the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish."""

    def fly(self):
        """Make the flying fish soar."""
        print("The flying fish is soaring!")

    def swim(self):
        """Make the flying fish swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Describe the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
