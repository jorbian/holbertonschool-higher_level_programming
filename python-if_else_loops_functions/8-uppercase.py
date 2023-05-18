#!/usr/bin/python3


def uppercase(str):

    value_of_a = 97
    length_of_alphabet = 26
    difference = 32

    characters = [x for x in str]

    message = "".join([
        y if ord(y) < (
            value_of_a or ord(y) > value_of_a + length_of_alphabet
         ) else
        chr(ord(y) - difference) for y in characters
        ]
    )
    print("{}".format(message))
