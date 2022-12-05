import string

N_STACKS = 9

STACKS_FILENAME = 'input1.txt'
MOVES_FILENAME = 'input2.txt'

with open(STACKS_FILENAME) as f:
    input_lines = f.readlines()

input_col2stack_idx = {(i * 4 + 1): (i + 1) for i in range(N_STACKS)}

class SingleStack:
    def __init__(self, idx: int) -> None:
        self.idx = idx
        self.stack = []

    def add_element(self, element: str):
        self.stack.append(element)

    def pop_element_from_top(self):
        removed_element = self.stack.pop()
        return removed_element

    def reverse_order(self):
        self.stack.reverse()

class StackManager:
    def __init__(self, n_stacks: int) -> None:
        self.stacks = {}
        self.n_stacks = n_stacks
        for i in range(self.n_stacks):
            self.stacks[i + 1] = SingleStack(i)

    def reverse_all_stacks(self):
        for i in range(self.n_stacks):
            self.stacks[i + 1].reverse_order()


manager = StackManager(N_STACKS)

for line in input_lines:
    for idx, element in enumerate(line):
        if element in string.ascii_letters:
            stack_idx = input_col2stack_idx[idx]
            manager.stacks[stack_idx].add_element(element)

manager.reverse_all_stacks()


with open(MOVES_FILENAME) as f:
    input_lines = f.readlines()
    
quantity_idx, origin_idx, destination_idx = 1, 3, 5

for line in input_lines:

    elements_in_line = line.strip().split(' ')
    quantity = int(elements_in_line[quantity_idx])
    origin = int(elements_in_line[origin_idx]) 
    destination = int(elements_in_line[destination_idx])

    for _ in range(quantity):
        element = manager.stacks[origin].pop_element_from_top()
        manager.stacks[destination].add_element(element)

output = [stack.stack[-1] for stack in manager.stacks.values()]
output = ''.join(output)
print(output)