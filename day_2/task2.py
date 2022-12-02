from dataclasses import dataclass
INPUT_FILE = 'input.txt'

@dataclass
class OutcomePoints:
    draw = 3
    win = 6
    lose = 0

@dataclass
class ShapePoints:
    rock = 1
    paper = 2
    scissors = 3

# A rock
# B paper
# C scissors

# X lose
# Y draw
# Z win
shape2points = {
    'A X': ShapePoints.scissors,
    'A Y': ShapePoints.rock,
    'A Z': ShapePoints.paper,
    'B X': ShapePoints.rock,
    'B Y': ShapePoints.paper,
    'B Z': ShapePoints.scissors,
    'C X': ShapePoints.paper,
    'C Y': ShapePoints.scissors,
    'C Z': ShapePoints.rock
}

outcome2points = {
    'X': OutcomePoints.lose,
    'Y': OutcomePoints.draw,
    'Z': OutcomePoints.win
}

with open(INPUT_FILE, 'r') as f:
    content = f.readlines()

sum_of_points = 0
for line in content:
    line = line.strip()
    opponent_shape, outcome = line.split(' ')
    try:
        single_round_points = shape2points[line] + outcome2points[outcome]
        sum_of_points += single_round_points
    except Exception as e:
        print(e)

print('Sum of points:')
print(sum_of_points)


