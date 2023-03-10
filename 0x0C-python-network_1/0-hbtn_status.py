#!/usr/bin/python3

import urllib.request


def display_response_body(response):
    """THE REAL SUBSTANCE OF THIS TASK"""
    display_template = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""

    if response is not None:
        response_body = response.read()
        print(
            display_template.format(
                type(response_body),
                response_body,
                response_body.decode("utf-8")
            )
        )


def do_something_to_page(url, retreval_func, thing_func):
    """ATTEMPTING TO TAKE RECYCLABLE FUNCTIONAL APPROACH"""
    with retreval_func(url) as page:
        thing_func(page)


if __name__ == "__main__":
    do_something_to_page(
        url="https://intranet.hbtn.io/status",
        retreval_func=urllib.request.urlopen,
        thing_func=display_response_body
    )
