#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
"""
import sys
import urllib.parse
import urllib.request


def exchange_packets(request, make, do_thing):
    with make(request) as response:
        result = do_thing(response)


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    exchange_packets(
        urllib.request.Request(
            url,
            urllib.parse.urlencode(
                value
            ).encode("ascii")
        ),
        urllib.request.urlopen,
        (lambda x: print(getattr(getattr(x, "read"(), "decode")("utf-8"))))
    )
