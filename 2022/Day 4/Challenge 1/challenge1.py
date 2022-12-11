# Day 4, challenge 1 of AoC22
# Challenge 1 - For a pairs of ranges of numbers, identify ranges that are a subset of each other ( {2, 3, 4} is completely contained in {1, 2, 3, 4, 5, 6}).

# We know that a range is a subset of another range if its borders are smaller or equal to the borders 
# of said other range => (1 - 2) subset of (0 - 3). By doing the difference between the starting positions 
# and ending position of each range, we get to modelise that relationship in an easier fashion. Following matrix 
# details the logic : 
# * Where diff_start, diff_end = range1[0] - range2[0], range1[1] - range2[1] *
# +------------+-------+-------+-------+
# | diff_end   |       |  > 0  |  < 0  |
# | ---------- |   0   | (pos) | (neg) |
# | diff_start |       |       |       |
# +============+=======+=======+=======+
# |      0     |  +1   |  +1   |  +1   |
# +------------+-------+-------+-------+
# |    > 0     |       |       |       |
# |    (pos)   |  +1   |  +0   |  +1   |
# +------------+-------+-------+-------+
# |    < 0     |       |       |       |
# |    (neg)   |  +1   |  +1   |  +0   |
# +------------+-------+-------+-------+
# The product of a negative diff_start or diff_end with a positive diff_start or diff_end will always be negative;
# if diff_start or diff_end = 0, we increment. Hence why we check if the product is <= 0 to determine if its a subset.
def range_contains_subset(range1: tuple, range2: tuple) -> bool:
    return (range1[0] - range2[0]) * (range1[1] - range2[1]) <= 0

with open('../input') as f:
    count_subsets = 0

    # Iterate over input
    for line in f.readlines():
        # Extract both ranges from line in the form of ints
        range1, range2 = [tuple(int(sub_range) for sub_range in str_range.split('-')) for str_range in line.rstrip('\n').split(',')]

        # Increment counter
        if range_contains_subset(range1, range2):
            count_subsets += 1

    # Challenge 1 answer
    print('Challenge 1 : Number of assignement pairs where one range fully contains the other ' + str(count_subsets))