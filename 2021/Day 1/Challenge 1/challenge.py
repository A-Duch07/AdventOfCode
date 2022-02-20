input = open("../input", "r")
count = -1
prevDepth = float('-inf')

for depth in input: 
    if prevDepth < int(depth):
        count += 1
    prevDepth = int(depth)

print(count)