# Day 1, challenge 2 of AoC2024 - Determine the similarity score between two lists
# For each number in the left list, find its duplicates in the right list. Then multiply 
# the number of duplicates by the left list number. So say 3 appears 3 times, then that's 9.
# Do the sum of all the similarity scores between lists.
with open('../input') as f:
    # Create two empty lists and then process the input to fill in the right and left lists
    right_list, left_list = ([], [])
    for index, value in enumerate(f):
        left_value, right_value = map(int, value.split())
        right_list.append(right_value)
        left_list.append(left_value)

    # Iterate through each value in the right and left lists and count the number of times they are present
    duplicates_right_list = dict([(value, right_list.count(value)) for value in right_list])
    duplicates_left_list = dict([(value, left_list.count(value)) for value in left_list])

    # Iterate through the left list and create a similarity score through a dict
    similarity_scores_per_value = dict()
    for left_value, count in duplicates_left_list.items():
        # If the left_value is in the right list (as a key of duplicates_right_list), then the similarity score
        # for the left_value is equal to the product with the number of occurences in the right list
        if left_value in duplicates_right_list:
            similarity_scores_per_value[left_value] = count * left_value * duplicates_right_list[left_value]
        else:
            # 0 when the left_value isn't in the right list
            similarity_scores_per_value[left_value] = 0
    
    # Determine the sum between the sorted lists
    sum_of_similarities = sum(similarity_scores_per_value.values())
    print(sum_of_similarities)