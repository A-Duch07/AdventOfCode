# Day 6, challenge 2 of AoC22
# Challenge 2 - Find the position of the start of message marker (ie, position of first 14 different chars)

with open('../input') as f:
    # Initial solution
    solution = -1
    # Buffer for the chars
    buffer = []

    # Iterate over the chars of our input
    for idx, char in enumerate(f.readline()):
        # Check that the char isn't in our current buffer
        # If it isn't in the buffer, append it 
        # Else, we create a new buffer ranging from the index+1 of the identical char to the end of the buffer
        # Ex. : buffer => [a, b, c] and char => b, then buffer becomes => [c]
        if char not in buffer:
            buffer.append(char)
        else : 
            char_idx = buffer.index(char)
            buffer = buffer[char_idx+1:]
            buffer.append(char)

        if len(buffer) == 14: 
            solution = idx + 1
            break

    # Challenge 1 answer
    print('Challenge 1 : ' + str(solution))