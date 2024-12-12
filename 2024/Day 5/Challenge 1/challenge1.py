# Day 5, challenge 1 of AoC2024 - there are problems with a printing queue for pages. We have a set of
# ordering rules for pages in a printer update that have to be respected in order for a printer update
# to be valid. The input look something like this:
# 47|53
# 97|13
# 97|61
#
# 75,47,61,53,29
# 97,61,53,29,13
# 
# Each set of X|Y represents a number X to be printed before Y if they are in the same update.
# The subsequent lists of number represent printer updates and their page ordering.
# The objective is to determine all the safe updates, and add their middle page numbers together.

import math as m

with open('../input') as f:
    # Extract the input into two seperate lists to be processed accordingly
    puzzle_input: str = f.read()
    seperator: int = puzzle_input.find('\n\n')
    ordering_rules: list[tuple[int]] = list(map(lambda value: tuple(map(int, value.split('|'))), puzzle_input[:seperator].splitlines()))
    updates: list[list[int]] = list(map(lambda value: list(map(int, value.split(','))), puzzle_input[seperator:].strip().splitlines()))

    # For each update in the update least
    count: int = 0
    for update in updates:
        safe_update: bool = True # Assume its safety at first
        for idx, page in enumerate(update[:-1]):
            # If any combo of a page set to be printed later in the update (sub_page) and 
            # the current page figure in the ordering rules, that means one rule is broken
            if any((sub_page, page) in ordering_rules for sub_page in update[idx+1:]):
                safe_update = False
                break
        # Find the middle eleme of each safe update and add to the count
        if safe_update:
            count += update[m.floor(len(update)/2)] # Assuming updates are odd in length
    
    print(count)