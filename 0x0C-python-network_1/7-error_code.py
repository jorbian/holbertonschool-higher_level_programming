#!/usr/bin/python3
"""SENDS REQUEST TO A GIVEN URL AND DISPLAYS THE RESPONSE BODY.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    
    message_strings = [
        ((r.status_code >= 400), ("Error code: {}".format(r.status_code))),
        (True, r.text)
    ]
    for test in message_strings:
        if test[0]:
            display_s = test[1]
            break
        
    print(display_s)