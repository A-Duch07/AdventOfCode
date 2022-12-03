# Day 3, challenge 1 of AoC22
# Challenge 1 - sum of priorities for items appearing in both compartments of rucksack
import numpy as np
import pandas as pd
import string

type_priorities = pd.Series(range(1, 53), index = list(string.ascii_lowercase + string.ascii_uppercase))

# Identifies duplicate and returns its priority
def identify_duplicate(rucksack: str) -> int:
    # Separate the string into its compartments 
    compartment_length = int(len(rucksack)/2)
    compartment1, compartment2 = tuple(rucksack[idx: idx + compartment_length] for idx in range(0, compartment_length + 1, compartment_length))

    # Return the priority of the common type in both compartments
    for type in compartment1: 
        if type in compartment2:
            return type_priorities[type]

    # Return 0 if no common type is found, which won't impact the sum of the priorities
    return 0

# Iterate over the file to determine the sum of the priorities for each duplicate among compartments
with open('../input') as f:
    # Get all the rucksacks -> [strings], identify the duplicates [ints] and then sum the priorities of the duplicates
    solution = pd.Series([line.rstrip('\n') for line in f.readlines()]).apply(identify_duplicate).sum()

    # Challenge 1 answer
    print('Challenge 1 : ' + str(solution))