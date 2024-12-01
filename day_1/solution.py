import time
from typing import List
from utils.extract_data_from_file import extract_data_from_file
from utils.get_list_of_lines import get_list_of_lines
from utils.SolutionResults import SolutionResults


def separate_row(row: str) -> List[int]:
    if row != "":
        numbers = row.split("   ")
        return [int(numbers[0]), int(numbers[1])]
    else:
        return []


def create_lists(rows: List[str]) -> dict[str, List[int]]:
    lists: dict[str, List[int]] = {
        "first_list": [],
        "second_list": [],
    }
    for row in rows:
        elements = separate_row(row)
        if len(elements) != 0:
            lists["first_list"].append(elements[0])
            lists["second_list"].append(elements[1])
    lists["first_list"].sort()
    lists["second_list"].sort()
    return lists


def get_list_differences(lists: dict[str, List[int]]) -> List[int]:
    differences: List[int] = []
    for i in range(len(lists["first_list"])):
        differences.append(abs(lists["first_list"][i] - lists["second_list"][i]))
    return differences


def sum_differences(differences: List[int]) -> int:
    total = 0
    for i in range(len(differences)):
        total += differences[i]
    return total


def solve_problem(is_official: bool) -> SolutionResults:
    start_time = time.time()
    data = extract_data_from_file(1, is_official)
    rows = get_list_of_lines(data)
    lists = create_lists(rows)
    differences = get_list_differences(lists)
    total = sum_differences(differences)
    part_1 = total
    part_2 = len(rows)
    end_time = time.time()
    execution_time = end_time - start_time
    results = SolutionResults(1, part_1, part_2, execution_time)
    return results
