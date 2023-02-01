#!/usr/bin/python3

"""AN EMPTY CLASS"""


class BaseGeometry:
    """ALL THE GOOD STUFF WILL EVENTUALLY GO HERE"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
