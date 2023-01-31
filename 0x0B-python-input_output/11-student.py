#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """EXACTLY WHAT IT SAYS ON THE TIN"""

    def __init__(self, first_name, last_name, age):
        """INITALIZE """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary represntation of a simple data structure."""
        if (
            isinstance(attrs, list) and all(isinstance(ele, str))
            for ele in attrs
        ):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
