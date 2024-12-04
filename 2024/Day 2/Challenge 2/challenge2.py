# Day 2, challenge 2 of AoC2024 - Identical to the previous challenge, except that now, 
# when the report is deemed unsafe, you can reevaluate it while having removed only one 
# level. If the removal of a single level makes it safe, then the report is deemed safe
# after all.
import copy

def evalute_report(report:list[int]) -> bool:
        # Instantiate booleans and int for safety assessment of report
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

        return safe

with open('../input') as f:
    # Iterate through each report on the provided nuclear plant list. Determine the safety of reports
    safety_reports: list[bool] = [] 
    for value in f:
        # Extract each report from the input (i.e. a line of the input)
        report: list = list(map(int, value.split()))

        # Verify safety of the report
        safe = evalute_report(report)

        # If it isn't safe, verify safety upon removal of current or next level
        if not safe:
            # Copy the report list and then delete the appropriate items
            test_reports: list[list[int]] = [copy.deepcopy(report) for _ in range(len(report))]
            for index, report in enumerate(test_reports):
                del report[index]

                # Delete each value of a report and reevaluate it to see if its safe
                if evalute_report(report):
                    safe = True
                    break

        # Append the safety of each report
        safety_reports.append(safe)

    print(sum(safety_reports))