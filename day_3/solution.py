import time
from re import findall
from utils.extract_data_from_file import extract_data_from_file
from utils.SolutionResults import SolutionResults


def find_all_mul_expressions(corrupted_input: str) -> list[str]:
    mul_pattern = r"mul\(\d+,\d+\)"
    mul_expressions = findall(mul_pattern, corrupted_input)
    return mul_expressions


def remove_all_off_blocks(corrupted_input: str) -> str:
    on_input = ""
    current_index = 0
    any_dont_left = True
    while current_index < len(corrupted_input) and any_dont_left:
        first_dont = corrupted_input[current_index:].find("don't()")
        first_do_after_dont = corrupted_input[first_dont:].find("do()") + first_dont
        on_input += corrupted_input[current_index:first_dont]
        current_index = first_do_after_dont
        any_dont_left = corrupted_input[current_index:].find("don't()") != -1
        print("CURRENT INDEX:", current_index)
        print("ANY DON'T LEFT:", any_dont_left)
    on_input += corrupted_input[current_index:]
    return on_input


def multiply_values_in_expression(expression: str) -> int:
    sections = expression.split(",")
    first_number = int(sections[0][4:])
    second_number = int(sections[1][:-1])
    product = first_number * second_number
    return product


def sum_all_products(corrupted_input: str) -> int:
    total = 0
    expressions = find_all_mul_expressions(corrupted_input)
    for expression in expressions:
        product = multiply_values_in_expression(expression)
        total += product
    return total


def sum_all_products_excluding_off_blocks(corrupted_input: str) -> int:
    total = 0
    only_on = remove_all_off_blocks(corrupted_input)
    expressions = find_all_mul_expressions(only_on)
    for expression in expressions:
        product = multiply_values_in_expression(expression)
        total += product
    return total


def solve_problem(is_official: bool) -> SolutionResults:
    start_time = time.time()
    data = extract_data_from_file(3, is_official)
    part_1 = sum_all_products(data)
    part_2 = sum_all_products_excluding_off_blocks(data)
    end_time = time.time()
    execution_time = end_time - start_time
    results = SolutionResults(3, part_1, part_2, execution_time)
    return results
