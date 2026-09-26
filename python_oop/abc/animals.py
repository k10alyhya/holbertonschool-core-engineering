#!/usr/bin/env python3
"""This module defines Animal, Dog, and Cat classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent an abstract animal."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
