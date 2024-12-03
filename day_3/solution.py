import time
from re import findall
from utils.extract_data_from_file import extract_data_from_file
from utils.SolutionResults import SolutionResults


def find_all_mul_expressions(corrupted_input: str) -> list[str]:
    mul_pattern = r"mul\(\d+,\d+\)"
    mul_expressions = findall(mul_pattern, corrupted_input)
    return mul_expressions


def multiply_values_in_expression(expression: str) -> int:
    sections = expression.split(",")
    first_number = int(sections[0][4:])
    second_number = int(sections[1][:-1])
    product = first_number * second_number
    return product


def sum_all_products(data: str) -> int:
    total = 0
    expressions = find_all_mul_expressions(data)
    for expression in expressions:
        product = multiply_values_in_expression(expression)
        total += product
    return total


def solve_problem(is_official: bool) -> SolutionResults:
    start_time = time.time()
    data = extract_data_from_file(3, is_official)
    part_1 = sum_all_products(data)
    part_2 = len(data)
    end_time = time.time()
    execution_time = end_time - start_time
    results = SolutionResults(3, part_1, part_2, execution_time)
    return results
