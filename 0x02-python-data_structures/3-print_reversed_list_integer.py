#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()

    for x in my_list:
        print("{:d}".format(x))

if __name__ == "__main__":
    foo = [1,2,3,4]
    print_reversed_list_integer(foo)
