# Day 4, challenge 2 of AoC2024 - Instead of checking for XMAS or SAMX like in previous challenge,
# this time we are checking for an X-shaped MAS or SAM, like so:
# M.S
# .A.
# M.S
# Count the number of occurences of the X-shaped MAS/SAM.

# Comparison function for MAS and SAM
def assertCross(value: list[str]) -> bool:
    mas: list[str] = ['M', 'A', 'S']
    sam: list[str] = ['S', 'A', 'M']
    return True if all(v == x for v, x in zip(value, mas)) or all(v == x for v, x in zip(value, sam)) else False


with open('../input') as f:
    # Readlines into a list of strings
    puzzle: list[str] = f.read().splitlines()
    count:int = 0

    # Iterate through each line of the input and every individual character
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            # If the character is A, check for X-shaped MAS/SAM
            # Note that checking any other character doesn't work as simply, 
            # as they may appear a number of times and we'd have duplicates
            if char == 'A':
                # Get both crosses of the X, and compare against the strings MAS and SAM
                if i-1>=0 and i+1<len(puzzle) and j-1>=0 and j+1<len(line):
                    assertion: bool = assertCross([puzzle[i+k][j+k] for k in range(-1, 2)]) and assertCross([puzzle[i+k][j-k] for k in range(-1, 2)])
                    count += 1 if assertion else 0

    print(count)