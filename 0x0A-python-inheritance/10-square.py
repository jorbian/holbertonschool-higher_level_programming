#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle.py').BaseGeometry


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
