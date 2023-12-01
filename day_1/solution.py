def solution():
    chunk = extract_data_from_file()
    lines = break_chunk_into_lines(chunk)
    all_number_arrays = []
    total = 0
    for line in lines:
        numbers_in_line = find_all_numbers_in_line(line)
        all_number_arrays.append(numbers_in_line)
    for number_array in all_number_arrays:
        row_number = combine_first_and_last_numbers_from_line_into_new_number(number_array)
        total += row_number
    return total

def combine_first_and_last_numbers_from_line_into_new_number(all_numbers: [int]):
    first_number = all_numbers[0]
    last_number = all_numbers[-1]
    composite_string = str(first_number) + str(last_number)
    composite_number = int(composite_string)
    return composite_number

def find_all_numbers_in_line(line: str):
    numbers_in_line = []
    for character in line:
        if character.isdigit():
            numbers_in_line.append(character)
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