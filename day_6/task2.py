INPUT_FILE = 'input.txt'
WINDOW_LEN = 14

with open(INPUT_FILE) as f:
    input_lines = f.readlines()

for i in input_lines:
    i.strip()

input_sequence = input_lines[0]

for i in range(len(input_sequence)):
    start = i
    end = i + WINDOW_LEN

    letters_in_window = input_sequence[start: end]
    if len(set(letters_in_window)) == len(letters_in_window):
        print(f'Start of marker at {end}')
        break

