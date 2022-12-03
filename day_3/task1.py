import string

letters = string.ascii_letters
letter2num = {letter: value + 1 for value, letter in enumerate(letters)}

INPUT_DATA = 'input.txt'

with open(INPUT_DATA, 'r') as f:
    lines = f.readlines()

sum_of_letter_values = 0

for line in lines:
    line = line.strip()
    line_len = len(line)
    half_of_line_len = line_len // 2
    first_part, second_part = line[:half_of_line_len], line[half_of_line_len:]
    assert len(first_part) + len(second_part) == line_len

    chars_in_first_part = set([i for i in first_part])
    chars_in_second_part = set([i for i in second_part])

    common_chars = chars_in_first_part.intersection(second_part)
    value_of_chars = sum([letter2num[i] for i in common_chars])
    sum_of_letter_values += value_of_chars

print(sum_of_letter_values)