# Day 3, challenge 1 of AoC2024 - We are provided a list of corrupted instructions from a programs memory. It looks like:
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)) = 161
# The only operation that is legitimate in said list of instruction is any operation that matches mul(x, y), where x and y
# can be anywhere from 1 to 3 digits long. Find all operations and do the sum of all products.
import re

with open('../input') as f:
    # Extract a list of operations based on the regex that matches mul(x, y), where x and y can be anywhere from 1 to 3 digits long
    operations: list[str] = re.findall(r'mul\(\d{1,3},\d{1,3}\)', f.read())

    # For each operation in the input, strip it of its mul() operator, split it based on the comma to get both values to multiply, turn them into
    # ints and create a list of tuples to be multiplied together. Map the list of tuples by multiplying their operands and the do the sum of said map.
    print(sum(map(lambda operands: operands[0] * operands[1], [tuple(map(int, operation.strip('mul()').split(','))) for operation in operations])))
        