from dataclasses import dataclass
INPUT_FILE = 'input.txt'

@dataclass
class OutcomePoints:
    draw = 3
    win = 6
    lose = 0

@dataclass
class ShapePoints:
    x = 1
    y = 2
    z = 3

possible_outcomes = {
    'A X': OutcomePoints.draw,
    'A Y': OutcomePoints.win,
    'A Z': OutcomePoints.lose,
    'B X': OutcomePoints.lose,
    'B Y': OutcomePoints.draw,
    'B Z': OutcomePoints.win,
    'C X': OutcomePoints.win,
    'C Y': OutcomePoints.lose,
    'C Z': OutcomePoints.draw
}

possible_shapes = {
    'X': ShapePoints.x,
    'Y': ShapePoints.y,
    'Z': ShapePoints.z
}

with open(INPUT_FILE, 'r') as f:
    content = f.readlines()

sum_of_points = 0
for line in content:
    line = line.strip()
    opponent_shape, my_shape = line.split(' ')
    try:
        single_round_points = possible_outcomes[line] + possible_shapes[my_shape]
        sum_of_points += single_round_points
    except Exception as e:
        print(e)

print('Sum of points:')
print(sum_of_points)


