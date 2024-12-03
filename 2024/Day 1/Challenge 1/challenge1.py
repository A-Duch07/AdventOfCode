# Day 1, challenge 1 of AoC2024 - Add the distance between sorted list pairs
# (i.e. if the smallest item of one list is 10, and the smallest from the
# second list is 15, the distance is 5)
with open('../input') as f:
    # Create two lists and then process the input to fill in the right and left lists
    right_list, left_list = ([], [])
    for index, value in enumerate(f):
        left_value, right_value = map(int, value.split())
        right_list.append(right_value)
        left_list.append(left_value)

    # Determine the sum between the sorted lists
    sum_of_differences = sum([abs(i-j) for i, j in zip(sorted(right_list), sorted(left_list))])
    print(sum_of_differences)