#!/usr/bin/python3


def fizzbuzz(
    factors=[
        {
            "word": "Fizz",
            "num": 3
        },
        {
            "word": "Buzz",
            "num": 5
        },
        ]
):
    for x in range(1,101):

        say = ""

        for factor in factors:
            if (x % factor["num"] == 0):
                say += factor["word"]

        if (len(say) == 0):
            say = str(x)

        print("{} ".format(say), end="")
