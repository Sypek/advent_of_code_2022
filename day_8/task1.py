input_file = '/Users/kubasyp/Desktop/AoC/advent_of_code_2022/day_8/input.txt'

with open(input_file) as f:
    input_lines = f.readlines()


arr = [[int(element) for element in row.strip()] for row in input_lines]
    
print(arr)

n_rows = len(arr)
n_cols = len(arr[0])


class Observe:
    def __init__(self, row_idx, col_idx, arr) -> None:
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.lookup_value = arr[self.row_idx][self.col_idx]
        self.arr = arr

    def _look_left(self):
        neighbors = arr[self.row_idx][:self.col_idx]
        visible = all(True if n < self.lookup_value else False for n in neighbors)
        return visible

    def _look_right(self):
        neighbors = arr[self.row_idx][self.col_idx + 1:]
        visible = all(True if n < self.lookup_value else False for n in neighbors)
        return visible

    def _look_top(self):
        neighbors = [arr[i][self.col_idx] for i in range(n_rows)]
        neighbors = neighbors[:self.row_idx]
        visible = all(True if n < self.lookup_value else False for n in neighbors)
        return visible

    def _look_bottom(self):
        neighbors = [arr[i][self.col_idx] for i in range(n_rows)]
        neighbors = neighbors[self.row_idx + 1:]
        visible = all(True if n < self.lookup_value else False for n in neighbors)
        return visible

    def is_visible(self):
        return any([self._look_right(), self._look_left(), self._look_bottom(), self._look_top()])

counter = 0
for r in range(1, n_rows - 1):
    for c in range(1, n_cols - 1):
        obs = Observe(r, c, arr)
        if obs.is_visible():
            # print(f'Visible coordinates: [{r}, {c}] with value {arr[r][c]}')
            counter += 1

edges = 2 * n_cols + 2 * n_rows - 4

print(f'N = {edges + counter}')