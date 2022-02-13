# Process data
input = open("../input", "r")
rawData = []
processedData = []
for depth in input: 
    rawData.append(int(depth))

for i in range(2, len(rawData)): 
    processedData.append((rawData[i-2], rawData[i-1], rawData[i]))

# Counting of the increments
count = -1
prevDepthSum = float('-inf')
for tuple in processedData: 
    (a, b , c) = tuple
    sum = a + b + c
    if prevDepthSum < sum:
        count += 1
    prevDepthSum = sum

print(count)