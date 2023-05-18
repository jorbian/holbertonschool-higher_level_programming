#!/usr/bin/env python3

import subprocess

from os.path import abspath
from pathlib import Path

THIS_FOLDER = Path(abspath(__file__)).parent

def fix_node_files(folder_obj):

    js_files = folder_obj.glob('*.js')
    for file in js_files:
        subprocess.run(["semistandard", "--fix", file.name])

if __name__ == "__main__":
    
    fix_node_files(THIS_FOLDER)