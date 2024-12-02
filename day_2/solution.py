import time
from typing import List
from utils.extract_data_from_file import extract_data_from_file
from utils.get_list_of_lines import get_list_of_lines
from utils.SolutionResults import SolutionResults


def extract_levels(report: str) -> List[int]:
    elements = report.split(" ")
    levels = [int(x) for x in elements]
    return levels


def determine_consistent_direction(vector: List[int]) -> bool:
    total_elements = len(vector)
    increases, decreases = 0, 0
    for i in range(total_elements - 1):
        if vector[i] < vector[i + 1]:
            increases += 1
        if vector[i] > vector[i + 1]:
            decreases += 1
    consistent = increases == 0 or decreases == 0
    return consistent


def determine_consistent_direction_with_dampener(vector: List[int], problems: int = 0) -> bool:
    if problems > 1:
        return False
    for i in range(len(vector) - 2):
        if (vector[i] < vector[i + 1] and vector[i + 1] > vector[i + 2]) or (vector[i] > vector[i + 1] and vector[i + 1] < vector[i + 2]):
            return determine_consistent_direction_with_dampener(vector[:i + 1] + vector[i + 2:], problems + 1)
    return True


def determine_acceptable_variance(vector: List[int]) -> bool:
    for i in range(len(vector) - 1):
        difference = abs(vector[i] - vector[i + 1])
        if difference == 0 or difference > 3:
            return False
    return True


def determine_acceptable_variance_with_dampener(vector: List[int], problems: int = 0) -> bool:
    if problems > 1:
        return False
    for i in range(len(vector) - 1):
        difference = abs(vector[i] - vector[i + 1])
        if difference == 0 or difference > 3:
            return determine_acceptable_variance_with_dampener(vector[:i] + vector[i + 1:], problems + 1)
    return True


def determine_safety(vector: List[int]) -> bool:
    consistent = determine_consistent_direction(vector)
    acceptable = determine_acceptable_variance(vector)
    safe = consistent and acceptable
    return safe


def determine_safety_with_dampener(vector: List[int]) -> bool:
    consistent = determine_consistent_direction_with_dampener(vector)
    acceptable = determine_acceptable_variance_with_dampener(vector)
    safe = consistent and acceptable
    return safe


def calculate_total_safe_reports(reports: List[str]) -> int:
    count = 0
    for report in reports:
        levels = extract_levels(report)
        safe = determine_safety(levels)
        if safe:
            count += 1
    return count


def calculate_total_safe_reports_with_dampener(reports: List[str]) -> int:
    count = 0
    for report in reports:
        levels = extract_levels(report)
        safe = determine_safety_with_dampener(levels)
        if safe:
            count += 1
    return count


def solve_problem(is_official: bool) -> SolutionResults:
    start_time = time.time()
    data = extract_data_from_file(2, is_official)
    rows = get_list_of_lines(data)
    part_1 = calculate_total_safe_reports(rows)
    part_2 = calculate_total_safe_reports_with_dampener(rows)
    end_time = time.time()
    execution_time = end_time - start_time
    results = SolutionResults(2, part_1, part_2, execution_time)
    return results
