# Day 3, challenge 2 of AoC2024 - We are provided a list of corrupted instructions from a programs memory. It looks like:
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)) = 161
# The only operation that is legitimate in said list of instruction is any operation that matches mul(x, y), where x and y
# can be anywhere from 1 to 3 digits long. Find all operations and do the sum of all products.
import re

with open('../input') as f:

    # Extract the position of all the do() and dont() instructions, marking the do() instructions as True and the dont() as False.
    # Sort all the instructions based on their position (we take the end of a do() instruction as we want what's after it, and the
    # beginning of a dont() instruction as we do not want anything that comes after it - including it)
    memory = f.read()
    delimiters: list[tuple] = [(delim.span()[1], True)for delim in re.finditer(r'(do\(\))', memory)] + [(delim.span()[0], False) for delim in re.finditer(r'(don\'t\(\))', memory)]
    delimiters.sort(key=lambda delimiters: delimiters[0])

    cleaned_memory: str = '' # All executable instructions
    exec_status: bool = True # Wether we currently are in executable or not state. Start as executable (or do())
    do_index: int = 0  # Index of the last do() instruction

    # Iterate through all the delimiters of do() and dont() instructions
    for current_index, current_exec_status in delimiters:
        # If there's a status change (exec->no exec or vice versa)
        if exec_status != current_exec_status:
            # If we are going from exec->no exec
            if exec_status:
                # Save the memory from the last do_index to the current_index (current_index represents a don't() instruction)
                cleaned_memory += ''.join(memory[do_index:current_index])
            else:
                #Else, when we just encounter a do() instruction, we update the do_index to the current_index value
                do_index = current_index
            
            # We always update the status when there's a status change
            exec_status = current_exec_status

    # If the last instruction was do(), then we save everything from that instruction to the end
    if exec_status:
        cleaned_memory += ''.join(memory[do_index:-1])

    # Extract a list of operations based on the regex that matches mul(x, y), where x and y can be anywhere from 1 to 3 digits long
    operations: list[str] = re.findall(r'mul\(\d{1,3},\d{1,3}\)', cleaned_memory)

    # For each operation in the input, strip it of its mul() operator, split it based on the comma to get both values to multiply, turn them into
    # ints and create a list of tuples to be multiplied together. Map the list of tuples by multiplying their operands and the do the sum of said map.
    print(sum(map(lambda operands: operands[0] * operands[1], [tuple(map(int, operation.strip('mul()').split(','))) for operation in operations])))
        