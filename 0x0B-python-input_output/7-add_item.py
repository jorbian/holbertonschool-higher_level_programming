#!/usr/bin/python3
"""Script that adds all arguments to list, and then save them to file"""

import sys
import json

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


def add_items():
    items = [x for x in sys.argv[1:]]

    with open("add_item.json", "w") as f:
        json.dump(items, f)

if __name__ == "__main__":
    add_items()
