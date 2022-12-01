# Day 1, challenge 1 and 2 of AOC2022 - counting calories for the elves
# Challenge 1 - number of calories for the elf with the most calories
# Challenge 2 - number of calories for the top 3 elves with the most calories (their sum)
from sortedcontainers import SortedList

# Instantiate two vars : sum_calories to contain the sum of calories for an elf;
# sorted_calories to contain the list of the sums of sorted calories for each elf.
sum_calories = 0
sorted_calories = SortedList()

# Iterate over the file to determine the sorted list of calories for the elves.
with open('./input') as f:
    # Get the contents of the input
    input = f.readlines()
    # Iterate over the input to sum the calories for each elf and sort them 
    for current_calories in input: 
        if current_calories != '\n':
            sum_calories += int(current_calories.strip('\n'))
        else : 
            sorted_calories.add(sum_calories)
            sum_calories = 0

    # readlines method doesn't return a line if its empty, so the last in put of the 
    # file, which is simply '\n', isn't in the input file and we never get to the else
    # for the last sum of calories! This fixes that
    sorted_calories.add(sum_calories)

# Challenge 1 answer
print('Challenge 1 : ' + str(sorted_calories[-1])) 

# Challenge 2 answer
print('Challenge 2 top 3 calories : ' + str(sorted_calories[-1:-4:-1]))
print('Challenge 2 sum of top 3 calories : ' + str(sum(sorted_calories[-1:-4:-1]))) 