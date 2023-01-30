#!/usr/bin/python3


def read_file(filename=""):
    if filename:
        with open(filename) as file:
            lines = file.readlines()
        print(lines)
