#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """EXACTLY WHAT IT SAYS ON THE TIN"""

    def __init__(self, first_name, last_name, age):
        """INITALIZE """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary represntation of a simple data structure."""
        return self.__dict__
