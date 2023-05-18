#!/usr/bin/python3


def roman_to_int(roman_string):

    digits = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "d": 1000
    }
    roman_string = roman_string.lower()

    invalid_input = not (
        all(x for x in list(digits.keys()) for x in roman_string) and
        len(roman_string) > 0
    )
    if invalid_input:
        return None