#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """Documetnation wuld go here."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
