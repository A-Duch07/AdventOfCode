# Day 3, challenge 2 of AoC22
# Challenge 2 - identify item type for each group, sum their priorities
import numpy as np
import pandas as pd
import string

type_priorities = pd.Series(range(1, 53), index = list(string.ascii_lowercase + string.ascii_uppercase))

# Splits input into their respective groups
def split_in_groups(rucksacks: list) -> list:
    return [(rucksacks[idx], rucksacks[idx+1], rucksacks[idx+2]) for idx in range(0, len(rucksacks), 3)]

# Identifies duplicate and returns its priority
def identify_duplicate(group: tuple) -> int:
    rucksack1, rucksack2, rucksack3 = group

    # Return the priority of the common type in all rucksacks for this group
    for type in rucksack1: 
        if type in rucksack2 and type in rucksack3:
            return type_priorities[type]

    # Return 0 if no common type is found, which won't impact the sum of the priorities
    return 0

# Iterate over the file to determine the sum of the priorities for each group
with open('../input') as f:
    # Get all the rucksacks -> [strings], split them in their groups [tuple(strings)], identify the badge within a group [ints] and then sum the priorities of the badges
    solution = pd.Series(split_in_groups([line.rstrip('\n') for line in f.readlines()])).apply(identify_duplicate).sum()

    # Challenge 2 answer
    print('Challenge 2 : ' + str(solution))