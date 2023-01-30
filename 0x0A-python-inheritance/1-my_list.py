#!/usr/bin/python3

"""Defines an inherited list class MyList."""



class MyList(list):
    """Documentation would go here"""
    def print_sorted(self):
        _t = self[:]
        _t.sort()
        print(_t)
