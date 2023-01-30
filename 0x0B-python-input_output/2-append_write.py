#!/usr/bin/python3

"""Define textfile-reading function."""


def append_write(filename="", text=""):
    """MORE DOCUMENATION WOULD GO HERe"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
