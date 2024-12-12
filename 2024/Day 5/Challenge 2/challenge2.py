# Day 5, challenge 2 of AoC2024 - Same challenge as the first one, but now we need to reorder printer updates
# that we're previously unsafe and return the sum of their middle pages.
import math as m

def sort_pages_by_rules(pages_to_sort: list[int], ordering_rules: list[tuple[int]]) -> list[int]:
    nb_items_to_sort: int = len(pages_to_sort)

    if len(pages_to_sort) > 2:
        # Split array in two when the length is bigger than two items and recursively call this function
        splitter: int = m.floor(nb_items_to_sort/2)
        sorted_first_half: list[int] = sort_pages_by_rules(pages_to_sort[:splitter], ordering_rules)
        sorted_second_half: list [int] = sort_pages_by_rules(pages_to_sort[splitter:], ordering_rules)

        # Join both lists together
        joined_list: list[int] = []
        # For each page in the 1st list, compare to the 2nd sorted list
        for page_1 in sorted_first_half:
            idx_to_del: list[int] = []
            for idx_2, page_2 in enumerate(sorted_second_half):
                # If the current page from the 2nd list comes before the current page from the 1st list 
                # ((page2, page1) is in our ordering list), add it to our joined_list and remove it from the 2nd list.
                if (page_2, page_1) in ordering_rules:
                    joined_list.append(page_2)
                    idx_to_del.append(idx_2)
            
            # Once we've finished comparing the current element from the 1st list with all those from the 2nd list, 
            # we add it to the newly joined list. Delete the appropriate pages from the second list, so as no 
            # to retiterate over them (start from the end of list not to cause idx out of bounds error when deleting)
            joined_list.append(page_1)
            for idx in idx_to_del[::-1]:
                del sorted_second_half[idx]

        # We add whatever is left in the 2nd sorted list to the newly joined list in case some values are left over
        joined_list += sorted_second_half
        return joined_list
    else:
        if len(pages_to_sort) > 1:
            if (pages_to_sort[1], pages_to_sort[0]) in ordering_rules:
                # Return the reversed list of pages to sort, as the 2nd item needs to come before the 1st
                return pages_to_sort[::-1]       
        # If there's only one item or they are correctly ordered, return the list as is
        return pages_to_sort

with open('../input') as f:
    # Extract the input into two seperate lists to be processed accordingly
    puzzle_input: str = f.read()
    seperator: int = puzzle_input.find('\n\n')
    ordering_rules: list[tuple[int]] = list(map(lambda value: tuple(map(int, value.split('|'))), puzzle_input[:seperator].splitlines()))
    updates: list[list[int]] = list(map(lambda value: list(map(int, value.split(','))), puzzle_input[seperator:].strip().splitlines()))

    count: int = 0
    for update in updates:
        reordered_array: list[int] = []
        for idx, page in enumerate(update[:-1]):
            if any((sub_page, page) in ordering_rules for sub_page in update[idx+1:]):
                # Already ordered part of the list is saved + newly sorted pages
                reordered_array += update[:idx] + sort_pages_by_rules(update[idx:], ordering_rules)
                count += reordered_array[m.floor(len(reordered_array)/2)]
                break 

    print(count)