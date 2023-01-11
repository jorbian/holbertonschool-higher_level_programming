#!/usr/bin/python3


if __name__ == "__main__":

    import sys

    num_of_args = len(sys.argv) - 1

    status = [
        None,
        "argument",
        "arguments"
    ][
        [
        num_of_args == 0,
        num_of_args == 1,
        num_of_args >= 2
        ].index(True)
    ]

    if status:

        print("{} {}:".format(num_of_args, status))

        for i in range(num_of_args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
    else:
        print("0 arguments.")