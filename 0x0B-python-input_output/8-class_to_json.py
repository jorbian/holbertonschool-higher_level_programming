#!/usr/bin/python3
"""function that returns the dictionary description of object for JSON"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__