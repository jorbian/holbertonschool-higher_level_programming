#!/usr/bin/python3

"""Define textfile-reading function."""


def write_file(filename="", text=""):
    """MORE DOCUMENATION WOULD GO HERe"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
