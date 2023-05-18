#!/usr/bin/python3

"""CLASS DOCUMENTATION GOES HERE"""


class Square:
    """REPRESENTATION OF A SQUARE WITH PRIVATE SIZE
    """

    def __init__(self, size=0):
        """CLASS CONSTRUCTOR FOR SQARE"
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    """RETURN THE AREA
    """
    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if (self.__size == 0):
            print("")
