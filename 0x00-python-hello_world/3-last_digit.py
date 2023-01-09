#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

last_digit = int((abs(number) % 10) * (number / abs(number)))

status_determiner = {
    (lambda x: x == 0): "and is 0",
    (lambda x: x > 5): "and is greater than 5",
    (lambda x: x < 6): "and is less than 6 and not 0"
}

for key, value in status_determiner.items():
    if (key(last_digit)):
        status = value

message = "Last digit of {} is {} {}".format(
    str(number),
    str(last_digit),
    status
)
print(message)
