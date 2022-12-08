input_file = '/Users/kubasyp/Desktop/AoC/advent_of_code_2022/day_8/input.txt'

with open(input_file) as f:
    input_lines = f.readlines()


arr = [[int(element) for element in row.strip()] for row in input_lines]
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
        neighbors.reverse()
        counter = 0
        for i in neighbors:
            if i == self.lookup_value:
                counter +=1
                break
            elif i < self.lookup_value:
                counter += 1
            else:
                counter += 1
                break
        return counter

    def _look_right(self):
        neighbors = arr[self.row_idx][self.col_idx + 1:]
        counter = 0
        for i in neighbors:
            if i == self.lookup_value:
                counter +=1
                break
            elif i < self.lookup_value:
                counter += 1
            else:
                counter += 1
                break
        return counter

    def _look_top(self):
        neighbors = [arr[i][self.col_idx] for i in range(n_rows)]
        neighbors = neighbors[:self.row_idx]
        neighbors.reverse()
        counter = 0
        for i in neighbors:
            if i == self.lookup_value:
                counter +=1
                break
            elif i < self.lookup_value:
                counter += 1
            else:
                counter += 1
                break
        return counter

    def _look_bottom(self):
        neighbors = [arr[i][self.col_idx] for i in range(n_rows)]
        neighbors = neighbors[self.row_idx + 1:]
        counter = 0
        for i in neighbors:
            if i == self.lookup_value:
                counter +=1
                break
            elif i < self.lookup_value:
                counter += 1
            else:
                counter += 1
                break
        return counter

    def multiplicator(self):
        left = self._look_left()
        right = self._look_right()
        top = self._look_top()
        bottom = self._look_bottom()
        multiplication = left * right * bottom * top
        # print('Right: ', right, 'left: ', left, 'top: ', top, 'bottom: ', bottom, 'multiplication: ', multiplication)
        return multiplication

max_value = 0
for r in range(1, n_rows - 1):
    for c in range(1, n_cols - 1):
        obs = Observe(r, c, arr)
        if obs.multiplicator() > max_value:
            max_value = obs.multiplicator()

print(max_value)