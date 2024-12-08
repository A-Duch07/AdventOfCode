# Day 4, challenge 1 of AoC2024 - Find string 'XMAS' in an input. It can be found horizontally 
# (both frontwards and backwards, i.e. XMAS and SMAX), vertically in both directions, and diagonally
# in all 4 directions. Count the number of occurence of said string.

# Comparison function for XMAS value
def assertXMAS(value: list[str]) -> int:
    xmas: list[str] = ['X', 'M', 'A', 'S']
    return 1 if all(v == x for v, x in zip(value, xmas)) else 0

with open('../input') as f:
    # Readlines into a list of strings
    puzzle: list[str] = f.read().splitlines()
    count:int = 0

    # Iterate through each line of the input and every individual character
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            if char == 'X':
                # Horizontal: use array splicing to check against XMAS and SAMX, easier this way
                count += (1 if line[j:j+4] == 'XMAS' else 0) + (1 if line[j-3:j+1] == 'SAMX' else 0)

                # Vertical: Can't use array splicing, so get the 4 chars above or below and 
                # use assertion function
                if i<len(puzzle)-3:
                    count += assertXMAS([puzzle[i+k][j] for k in range(4)])
                if i>2: 
                    count += assertXMAS([puzzle[i-k][j] for k in range(4)])
                
                # Diagonal left -> right: similarly to the vertical, get the diagonal that goes l->r
                # towards the bottom and top and check for XMAS
                if i<len(puzzle)-3 and j<len(line)-3: # l->r towards bottom
                    count += assertXMAS([puzzle[i+k][j+k] for k in range(4)])
                if i>2 and j<len(line)-3: # l->r towards top
                    count += assertXMAS([puzzle[i-k][j+k] for k in range(4)])

                # Diagonal right -> left: same as above, but right to left
                if i<len(puzzle)-3 and j>2: # r->l towards bottom
                    count += assertXMAS([puzzle[i+k][j-k] for k in range(4)])
                if i>2 and j>2: # r->l towards top
                    count += assertXMAS([puzzle[i-k][j-k] for k in range(4)])

    print(count)