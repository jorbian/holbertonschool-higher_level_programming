#!/usr/bin/python3

"""Wraper for test to see if object is of certain class"""


def is_same_class(obj, a_class):
    """Exactly what it says on the tin

    Args:
        obj (any): object to be checked
        a_class (type): the type we are checking for
    Returns:
        if it's of the target type - True
        otherwise - False
    """

    if type(obj) == a_class:
        return True
    return False
