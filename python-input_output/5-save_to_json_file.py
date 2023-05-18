#!/usr/bin/python3
"""Function that writes Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """MORE DOCUMENATION WOULD GO HERe"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
