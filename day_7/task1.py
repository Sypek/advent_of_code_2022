from collections import defaultdict 


def def_value():
    return 0

sizes = defaultdict(def_value)


def get_parents(path: str):
    elements = path.split('/')
    if len(elements) > 1:
        return ['/'.join(elements[: i+1]) for i in range(len(elements) - 1)]
    else:
        return []


class Tree:
    def __init__(self, current_dir: str) -> None:
        self.current_dir = current_dir

    def set_current_dir(self, name):
        if name != '..':
            self.current_dir = '/'.join([self.current_dir, name])
        else:
            self.current_dir = self.current_dir.rsplit('/', 1)[0]

class Steps:
    def __init__(self, tree: Tree) -> None:
        self.tree = tree

    def process_line(self, line: str):
        if line.startswith('$ cd'):
            destination = line.split(' ')[-1]
            self._process_move(destination)

        elif line.startswith('$ ls'):
            pass

        elif line[0].isdigit():
            self._process_file(line)

        elif line.startswith('dir'):
            pass
        else:
            raise Exception('WARNING')

    def _process_move(self, destination: str):
        self.tree.set_current_dir(destination)
        
    def _process_file(self, line: str):
        size, _ = line.split(' ')
        size = int(size)
        sizes[self.tree.current_dir] += size
        parents = get_parents(self.tree.current_dir)
        print(f'Parents of {self.tree.current_dir} are {parents}')
        for parent in parents:
            sizes[parent] += size
        

INPUT_FILE = '/Users/kubasyp/Desktop/AoC/advent_of_code_2022/day_7/input.txt'

with open(INPUT_FILE) as f:
    lines = f.readlines()

tree = Tree(current_dir='root')
steps = Steps(tree=tree)

for l in lines[1:]: # omit entering root dir
    l = l.strip()
    steps.process_line(l)
    


threshold = 100_000
sum_of_nodes = 0
for k, v in sizes.items():
    if v <= threshold:
        sum_of_nodes += v

print(sum_of_nodes)