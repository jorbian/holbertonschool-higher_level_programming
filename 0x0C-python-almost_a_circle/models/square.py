#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(
            self.__width,
            self.__height
        )
