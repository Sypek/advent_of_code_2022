INPUT_DATA = 'data1.txt'


def is_line_empty(line: str) -> bool:
    empty_line = '\n'
    if line == empty_line:
        return True
    else:
        False


def compare_scores_and_return_highest(previous_highest_score: int, current_score: int) -> int:
    return max(previous_highest_score, current_score)


with open(INPUT_DATA, 'r') as f:
    lines = f.readlines()

highest_score = 0
current_iter_score = 0

for l in lines:
    if is_line_empty(l):
        highest_score = compare_scores_and_return_highest(highest_score, current_iter_score)
        current_iter_score = 0
    else:
        this_line_score = int(l)
        current_iter_score += this_line_score

print('Highest score: ')
print(highest_score)