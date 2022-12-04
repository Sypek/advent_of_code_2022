from typing import Tuple

INPUT_FILE = 'input.txt'

with open(INPUT_FILE, 'r') as f:
    input_lines = f.readlines()


def get_interval_start_end_as_int(interval: str, delimiter='-') -> Tuple[int, int]:
    start, end = interval.split(delimiter)
    return int(start), int(end)


def check_if_intervals_overlap(first_interval: Tuple[int, int], second_interval: Tuple[int, int]):
    a_start, a_end = first_interval
    b_start, b_end = second_interval
    if (a_start <= b_start <= a_end) or (a_start <= b_end <= a_end) or (b_start <= a_start <= b_end) or (b_start <= a_end <= b_end):
        return True
    else:
        return False

overlapping_intervals_counter = 0

for line in input_lines:
    line = line.strip()
    interval_a, interval_b = line.split(',')

    a_start, a_end = get_interval_start_end_as_int(interval_a)
    b_start, b_end = get_interval_start_end_as_int(interval_b)

    if check_if_intervals_overlap((a_start, a_end), (b_start, b_end)):
        overlapping_intervals_counter += 1

print(overlapping_intervals_counter)