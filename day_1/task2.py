INPUT_DATA = 'data1.txt'


def is_line_empty(line: str) -> bool:
    empty_line = '\n'
    if line == empty_line:
        return True
    else:
        False


with open(INPUT_DATA, 'r') as f:
    lines = f.readlines()

all_scores = []
current_iter_score = 0

for l in lines:
    if is_line_empty(l):
        all_scores.append(current_iter_score)
        current_iter_score = 0
    else:
        this_line_score = int(l)
        current_iter_score += this_line_score

sorted_scores = sorted(all_scores, reverse=True)
top_3_scores = sorted_scores[:3]
top_3_scores_sum = sum(top_3_scores)

print('Top 3 scores:')
print(top_3_scores)
print(top_3_scores_sum)