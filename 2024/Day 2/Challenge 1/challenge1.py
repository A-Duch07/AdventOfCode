# Day 2, challenge 1 of AoC2024 - You're provided with an input that looks like:
# [7 6 4 2 1
#  1 2 7 8 9
#  9 7 6 2 1]
# Each row of the matrix represents a report that can be deemed safe or unsafe based
# on the levels in said report (individual values in the report, i.e. the ints). For
# a report to be safe, we need it to be either completely ascending or descending
# (so ordered) and we need for the difference between two adjacent levels to be no
# lesser than 1 or greater than 3. Determine the number of safe levels (2 safe, first and last
# on the test input).

with open('../input') as f:
    # Iterate through each report on the provided nuclear plant list. Determine the safety of reports
    safety_reports: list[bool] = [] 
    for value in f:
        # Extract each report from the input (i.e. a line of the input)
        report: list = list(map(int, value.split()))

        # Instantiate boolean and int for safety assessment of reports
        safe: bool = True
        previous_diff: int = 0
        for index, current_level in enumerate(report[:-1]):
            # Calculate the diff. between the next level and the current one
            next_level:int = report[index+1]
            diff_levels:int = current_level - next_level

            # If the previous diff. between levels is pos. or negative and the new diff. between levels has the same sign,
            # then the list is still either ascending or descending (like and AND operation. When previous diff. is 0, start of list). 
            # If the absolute value of the diff. between levels is between 0 and 4, then it respects the second rule of safety. 
            # Break if any rule isn't respected.
            if not ((previous_diff == 0 or ((previous_diff > 0) == (diff_levels > 0))) and 0 < abs(diff_levels) < 4):
                safe = False
                break

            # Reasign previous_diff before moving on
            previous_diff = diff_levels

        # Append the safety of each report
        safety_reports.append(safe)

    print(sum(safety_reports))