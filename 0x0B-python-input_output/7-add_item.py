#!/usr/bin/python3
"""Script that adds all arguments to list, and then save them to file"""

import sys
import json

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

items = sys.argv[1:]

with open("add_item.json", "w", encoding="utf-8") as file:
    json.dump(items, file)
