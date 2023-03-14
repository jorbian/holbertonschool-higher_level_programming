#!/usr/bin/python3
"""
AN EXPRIMENT WITH A FUNCTIONAL APPROACH TO TASK.
I WILL EVENTUALLY CLEAN THIS REPO UP TO TAKE BETTER ADVANTAGE OF IT/
"""
import sys
import urllib.request


def retrieve_header(url, header, do_action=(lambda x: x)):
    """IT NOT ONLY DOESNT CARE WHAT HEADER YOU WANT BUT WANT TO DO WITH IT"""
    with urllib.request.urlopen(url) as page:
        header = do_action(
            (page.headers).get(header)
        )
    return header


if __name__ == "__main__":
    url = sys.argv[1]
    retrieve_header(url, "X-Request-Id", print)
