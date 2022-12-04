from typing import Tuple

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    input_lines = f.readlines()


def get_interval_start_end_as_int(interval: str, delimiter='-') -> Tuple[int, int]:
    start, end = interval.split(delimiter)
    return int(start), int(end)


def check_if_first_interval_issubset_of_second(first_interval: Tuple[int, int], second_interval: Tuple[int, int]):
    if first_interval[0] >= second_interval[0] and first_interval[1] <= second_interval[1]:
        return True
    else:
        return False

overlapping_intervals_counter = 0

for line in input_lines:
    line = line.strip()
    interval_a, interval_b = line.split(',')

    a_start, a_end = get_interval_start_end_as_int(interval_a)
    b_start, b_end = get_interval_start_end_as_int(interval_b)

    if check_if_first_interval_issubset_of_second((a_start, a_end), (b_start, b_end)):
        overlapping_intervals_counter += 1
    elif check_if_first_interval_issubset_of_second((b_start, b_end), (a_start, a_end)):
        overlapping_intervals_counter += 1

print(overlapping_intervals_counter)