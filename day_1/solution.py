digits = [1,2,3,4,5,6,7,8,9,'one','two','three','four','five','six','seven','eight','nine']

def solution():
    chunk = extract_data_from_file()
    lines = break_chunk_into_lines(chunk)
    total = 0
    for line in lines:
        numbers_in_line = find_all_numbers_in_line(line)
        final_digit = combine_first_and_last_numbers_from_line_into_new_number(numbers_in_line)
        total += final_digit
    return total

def combine_first_and_last_numbers_from_line_into_new_number(numbers_array):
    first_and_last_numbers = determine_first_and_last_numbers_for_line(numbers_array)
    first_number = first_and_last_numbers[0]
    last_number = first_and_last_numbers[1]
    composite_string = str(first_number) + str(last_number)
    composite_number = int(composite_string)
    return composite_number

def determine_first_and_last_numbers_for_line(numbers_array):
    sorted_substrings = sorted(numbers_array, key=lambda x: x['index'])
    first_number_obj = sorted_substrings[0]
    last_number_obj = sorted_substrings[-1]
    first_number = first_number_obj['value'] if str(first_number_obj['value']).isdigit() else convert_string_to_number(first_number_obj['value'])
    last_number = last_number_obj['value'] if str(last_number_obj['value']).isdigit() else convert_string_to_number(last_number_obj['value'])
    return [first_number, last_number]

def convert_string_to_number(digit: str):
    if digit == 'one':
        return 1
    elif digit == 'two':
        return 2
    elif digit == 'three':
        return 3
    elif digit == 'four':
        return 4
    elif digit == 'five':
        return 5
    elif digit == 'six':
        return 6
    elif digit == 'seven':
        return 7
    elif digit == 'eight':
        return 8
    elif digit == 'nine':
        return 9

def find_all_numbers_in_line(line: str):
    numbers_in_line = []
    for digit in digits:
        index = line.find(str(digit))
        while index != -1:
            numbers_in_line.append({
                'value': digit,
                'index': index
            })
            index = line.find(str(digit), index + 1)
    return numbers_in_line

def break_chunk_into_lines(chunk: str):
    lines = chunk.split("\n")
    return lines

def extract_data_from_file():
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solution()
print(result)