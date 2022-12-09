input_file = 'input.txt'
from collections import defaultdict

with open(input_file) as f:
    input_lines = f.readlines()


class Position:
    def __init__(self, init_x_pos = 0, init_y_pos = 0) -> None:
        self.x = init_x_pos
        self.y = init_y_pos
        self.visited_positions = [(self.x, self.y)]

    def move(self, direction: str, n_steps: int):
        if direction == 'R':
            self._move_right(n_steps)
        elif direction == 'L':
            self._move_left(n_steps)
        elif direction == 'U':
            self._move_up(n_steps)
        elif direction == 'D':
            self._move_down(n_steps)

    def _move_right(self, n_steps: int):
        self.x += n_steps

    def _move_left(self, n_steps: int):
        self.x -= n_steps

    def _move_up(self, n_steps: int):
        self.y += n_steps

    def _move_down(self, n_steps: int):
        self.y -= n_steps

    def update_visited_positions(self):
        self.visited_positions.append((self.x, self.y))


def default_move():
    return [('R', 0)]


relative_xy_diff_to_tail_moves = defaultdict(default_move)
relative_xy_diff_to_tail_moves[(2, 0)] = [('R', 1)]
relative_xy_diff_to_tail_moves[(2, 1)] = [('R', 1), ('U', 1)]
relative_xy_diff_to_tail_moves[(2, -1)] = [('R', 1), ('D', 1)]

relative_xy_diff_to_tail_moves[(-2, 0)] = [('L', 1)]
relative_xy_diff_to_tail_moves[(-2, 1)] = [('L', 1), ('U', 1)]
relative_xy_diff_to_tail_moves[(-2, -1)] = [('L', 1), ('D', 1)]

relative_xy_diff_to_tail_moves[(0, 2)] = [('U', 1)]
relative_xy_diff_to_tail_moves[(1, 2)] = [('U', 1), ('R', 1)]
relative_xy_diff_to_tail_moves[(-1, 2)] = [('U', 1), ('L', 1)]

relative_xy_diff_to_tail_moves[(0, -2)] = [('D', 1)]
relative_xy_diff_to_tail_moves[(1, -2)] = [('D', 1), ('R', 1)]
relative_xy_diff_to_tail_moves[(-1, -2)] = [('D', 1), ('L', 1)]

relative_xy_diff_to_tail_moves[(2, 2)] = [('R', 1), ('U', 1)]
relative_xy_diff_to_tail_moves[(2, -2)] = [('R', 1), ('D', 1)]
relative_xy_diff_to_tail_moves[(-2, 2)] = [('L', 1), ('U', 1)]
relative_xy_diff_to_tail_moves[(-2, -2)] = [('L', 1), ('D', 1)]


class RelativePosition:
    def __init__(self, head_pos, tail_pos):
        self.head_pos = head_pos
        self.tail_pos = tail_pos

        self.x_diff = self.head_pos.x - self.tail_pos.x
        self.y_diff = self.head_pos.y - self.tail_pos.y
    
    def calculate_tail_moves(self) -> list:
        xy_diff = (self.x_diff, self.y_diff)
        moves = relative_xy_diff_to_tail_moves[(xy_diff)]
        return moves


head = Position()
tail = Position()


for line in input_lines:
    head_direction, head_n_steps = line.strip().split(' ')

    for step in range(int(head_n_steps)): # simulate step by step
        head.move(head_direction, 1)
        head.update_visited_positions()

        rel_pos = RelativePosition(head, tail)
        tail_moves = rel_pos.calculate_tail_moves()

        for tail_move in tail_moves:
            tail_direction, tail_steps = tail_move
            tail.move(tail_direction, tail_steps)
        tail.update_visited_positions()


n_tails = 9

previous_positions = tail.visited_positions

for tail_idx in range(n_tails - 1):
    tail = Position()
    for head_pos in previous_positions:
        head = Position(init_x_pos=head_pos[0], init_y_pos=head_pos[1])
        rel_pos = RelativePosition(head, tail)
        tail_moves = rel_pos.calculate_tail_moves()

        for tail_move in tail_moves:
            tail_direction, tail_steps = tail_move
            tail.move(tail_direction, tail_steps)
        tail.update_visited_positions()
    previous_positions = tail.visited_positions


visited_positions = tail.visited_positions
unique_visited_positions = list(set(visited_positions))

print(f'Number of unique visited positions: {len(unique_visited_positions)}')