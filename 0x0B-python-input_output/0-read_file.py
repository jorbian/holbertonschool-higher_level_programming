#!/usr/bin/python3

"""Define textfile-reading function."""


def read_file(filename=""):
    """MORE DOCUMENATION WOULD GO HERe"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
