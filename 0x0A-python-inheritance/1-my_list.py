#!/usr/bin/python3

"""Add a custom sorting method to a new list class"""


class MyList(list):
    """EXACTLY WHAT IT SAYS ON THE TIN"""

    def print_sorted(self):
        print(sorted(self))
