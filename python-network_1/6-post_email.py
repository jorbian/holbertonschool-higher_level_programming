#!/usr/bin/python3
"""SENDS 'POST' REQUEST TO GIVEN URL WITH EMAIL --
-- DISPLAYS THE BODY OF THE RESPNSE
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {
        "email": sys.argv[2]
    }
    request = requests.post(url, data=value)
    print(request.text)
