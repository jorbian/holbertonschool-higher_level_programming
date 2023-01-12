#!/usr/bin/python3


def print_list_integer(my_list=[]):
    for x in my_list:
        print("{}".format(x))

if __name__ == "__main__":
    foo = [1,2,3,4]
    print_list_integer(foo)
