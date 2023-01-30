#!/usr/bin/python3

"""Define textfile-reading function."""


def read_file(filename=""):
    """MORE DOCUMENATION WOULD GO HERe"""
    if filename:
        with open(filename, encoding="utf-8") as file:
            lines = file.readlines()
        print(lines)
