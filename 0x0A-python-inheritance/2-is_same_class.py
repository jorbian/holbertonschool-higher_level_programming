#!/usr/bin/python3

"""Wraper for test to see if object is of certain class"""

def is_same_class(obj, a_class):
    """Exactly what it says on the tin"""

    if type(obj) == a_class:
        return True
    return False
