#!/usr/bin/python3


def islower(c):
    value_of_a = 97
    length_of_alphabet = 26

    lowercase = (
        (ord(c) >= value_of_a) and (ord(c) <= value_of_a + length_of_alphabet)
    )
    return (lowercase)
