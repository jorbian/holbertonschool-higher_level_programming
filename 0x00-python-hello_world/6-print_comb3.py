#!/usr/bin/python3

unique_combinations = [
    list(z) for z in 
        [
        set(y) for y in 
            [
                set(x) for x in ["{:02d}".format(x) for x in range(1, 100)]
            ]
        ] if len(z) == 2
]
for combination in unique_combinations:
    combination.sort()

unique_combinations = [int(y) for y in set(["".join(x) for x in unique_combinations])]

unique_combinations.sort()

unique_combinations = ", ".join(
    "{:02d}".format(x) for x in
    unique_combinations
)
print(unique_combinations)
