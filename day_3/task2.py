import string

letters = string.ascii_letters
letter2num = {letter: value + 1 for value, letter in enumerate(letters)}

INPUT_DATA = 'input.txt'

with open(INPUT_DATA, 'r') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
sum_of_letter_values = 0

number_of_lines = len(lines)
group_len = 3

for idx in range(number_of_lines // group_len):
    start = idx * group_len
    end = start + 3
    lines_in_grooup = lines[start: end]
    first_line_letters = set([i for i in lines_in_grooup[0]])
    second_line_letters = set([i for i in lines_in_grooup[1]])
    third_line_letters = set([i for i in lines_in_grooup[2]])

    common_letters = first_line_letters.intersection(second_line_letters).intersection(third_line_letters)
    value_of_letters = sum([letter2num[i] for i in common_letters])
    sum_of_letter_values += value_of_letters

print(sum_of_letter_values)