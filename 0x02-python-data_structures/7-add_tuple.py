#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    input_tuples = [tuple_a, tuple_b]

    for tup in input_tuples:
        if (len(tup) < 2):
            tup = (tup[0], 0)
        elif (len(tup) > 2):
            tup = (tup[0], tup[1])

    output = (
        (input_tuples[0][0] + input_tuples[1][0]),
        (input_tuples[0][1] + input_tuples[1][1])
    )
    return (output)
