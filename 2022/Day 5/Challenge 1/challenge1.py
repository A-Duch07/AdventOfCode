# Day 5, challenge 1 of AoC22
# Challenge 1 - Perform the stack manipulation and then return the crates at the top of each stack
from collections import deque, defaultdict

def parse_input(input: list[str]) -> tuple:
    # Index to split the stacks from the list of operations in the input
    input_split = input.index('\n')

    # Get the unparsed stacks
    unparsed_stacks = [input[idx].rstrip('\n') for idx in range(input_split)]
    stack_idx_positions = [idx for idx, char in enumerate(unparsed_stacks.pop()) if char.isdigit()]

    # defaultdict to contain each stack for the input
    stacks = defaultdict(deque)
    for unparsed_stack in unparsed_stacks:
        for idx, pos in enumerate(stack_idx_positions): 
            if not unparsed_stack[pos].isspace():
                stacks[idx+1].append(unparsed_stack[pos])

    # Get the unparsed operations and extract the number of crates to unload as well as the source and target stacks
    unparsed_operations = [input[idx].rstrip('\n') for idx in range(input_split + 1, len(input))]
    operations = [tuple(int(chars) for chars in unparsed_operation.split() if chars.isdigit()) for unparsed_operation in unparsed_operations]

    return (stacks, operations)

with open('../input') as f:
    stacks, operations = parse_input(f.readlines())

    for operation in operations:
        number, source, target = operation
        for idx in range(number):
            stacks[target].appendleft(stacks[source].popleft())

    solution = ''.join([stacks[key].popleft() for key in sorted(stacks.keys())])

    # Challenge 1 answer
    print('Challenge 1 : ' + solution)