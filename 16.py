from enum import IntFlag
import os
from utils.runner import run_puzzle

class Connections(IntFlag):
    No = 0
    UP = 1
    RIGHT = 2
    DOWN = 4
    LEFT = 8
    UP2 = 16
    RIGHT2 = 32
    DOWN2 = 64
    LEFT2 = 128

COORDINATE_CHANGES = {
    Connections.UP: (-1, 0),
    Connections.UP2: (-1, 0),
    Connections.RIGHT: (0, 1),
    Connections.RIGHT2: (0, 1),
    Connections.DOWN: (1, 0),
    Connections.DOWN2: (1, 0),
    Connections.LEFT: (0, -1),
    Connections.LEFT2: (0, -1)
}

def opposite_connection(c: Connections):
    if c in (1,2,16,32):
        return Connections(c*4)
    else:
        return Connections(c//4)

def opposite(c: 'Pipe'):
    r = Connections(0)
    for ci in c.connections:
        r |= opposite_connection(ci)
    return r

def rotate(c: 'Pipe', left = False):
    r = Connections(0)
    if left:
        for ci in c.connections:
            if ci in (1,16):
                r |= ci*8
            else:
                r |= ci//2
    else:
        for ci in c.connections:
            if ci in (8,128):
                r |= ci//8
            else:
                r |= ci*2
    return r

CONNECTIONS_INDEX = {
    '│': Connections.UP | Connections.DOWN
    ,'┤': Connections.UP | Connections.DOWN | Connections.LEFT
    ,'╡': Connections.UP | Connections.DOWN | Connections.LEFT2
    ,'╢': Connections.UP2 | Connections.DOWN2 | Connections.LEFT
    ,'╖': Connections.DOWN2 | Connections.LEFT
    ,'╕': Connections.DOWN | Connections.LEFT2
    ,'╣': Connections.UP2 | Connections.DOWN2 | Connections.LEFT2
    ,'║': Connections.UP2 | Connections.DOWN2
    ,'╗': Connections.DOWN2 | Connections.LEFT2
    ,'╝': Connections.UP2 | Connections.LEFT2
    ,'╜': Connections.UP2 | Connections.LEFT
    ,'╛': Connections.UP | Connections.LEFT2
    ,'┐': Connections.DOWN | Connections.LEFT
    ,'└': Connections.UP | Connections.RIGHT
    ,'┴': Connections.UP | Connections.LEFT | Connections.RIGHT
    ,'┬': Connections.DOWN | Connections.LEFT | Connections.RIGHT
    ,'├': Connections.UP | Connections.DOWN | Connections.RIGHT
    ,'─': Connections.LEFT | Connections.RIGHT
    ,'┼': Connections.UP | Connections.DOWN | Connections.LEFT | Connections.RIGHT
    ,'╞': Connections.UP | Connections.DOWN | Connections.RIGHT2
    ,'╟': Connections.UP2 | Connections.DOWN2 | Connections.RIGHT
    ,'╚': Connections.UP2 | Connections.RIGHT2
    ,'╔': Connections.DOWN2 | Connections.RIGHT2
    ,'╩': Connections.UP2 | Connections.LEFT2 | Connections.RIGHT2
    ,'╦': Connections.DOWN2 | Connections.LEFT2 | Connections.RIGHT2
    ,'╠': Connections.UP2 | Connections.DOWN2 | Connections.RIGHT2
    ,'═': Connections.LEFT2 | Connections.RIGHT2
    ,'╬': Connections.UP2 | Connections.DOWN2 | Connections.LEFT2 | Connections.RIGHT2
    ,'╧': Connections.UP | Connections.LEFT2 | Connections.RIGHT2
    ,'╨': Connections.UP2 | Connections.LEFT | Connections.RIGHT
    ,'╤': Connections.DOWN | Connections.LEFT2 | Connections.RIGHT2
    ,'╥': Connections.DOWN2 | Connections.LEFT | Connections.RIGHT
    ,'╙': Connections.UP2 | Connections.RIGHT
    ,'╘': Connections.UP | Connections.RIGHT2
    ,'╒': Connections.DOWN | Connections.RIGHT2
    ,'╓': Connections.DOWN2 | Connections.RIGHT
    ,'╫': Connections.UP2 | Connections.DOWN2 | Connections.LEFT | Connections.RIGHT
    ,'╪': Connections.UP | Connections.DOWN | Connections.LEFT2 | Connections.RIGHT2
    ,'┘': Connections.UP | Connections.LEFT
    ,'┌': Connections.DOWN | Connections.RIGHT
}
CONNECTIONS_INDEX_REVERSE = {v: k for k, v in CONNECTIONS_INDEX.items()}
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up Right Down Left

class Pipe:
    def __init__(self, char: str, rotations = 0) -> None:
        self.char = char
        self.rotations = rotations
        self.final_orientation = False
        self.connections = self.get_connections()

    def __repr__(self) -> str:
        return f"{self.char}: {self.connections}"

    def get_connections(self) -> Connections:
        return CONNECTIONS_INDEX[self.char] if self.char in CONNECTIONS_INDEX else Connections.No
    
    def get_orientations(self) -> list['Pipe']:
        return_list: list[Pipe] = [self]
        r1 = Pipe(CONNECTIONS_INDEX_REVERSE[rotate(self)], 1)
        if r1.char == self.char:
            return return_list
        return_list.append(r1)
        r2 = Pipe(CONNECTIONS_INDEX_REVERSE[opposite(self)], 2)
        if self.char == r2.char:
            return return_list
        r3 = Pipe(CONNECTIONS_INDEX_REVERSE[rotate(self, True)], 3)
        return_list.append(r2)
        return_list.append(r3)
        return return_list
    
    def get_connections_for_all_orientations(self):
        if self.final_orientation:
            return set(self.connections)
        o = self.get_orientations()
        return_set: set[Connections] = set()
        for ori in o:
            return_set.update(ori.connections)
        return return_set

def valid_orientations(grid: list[list[Pipe]], row: int, col: int):
    pipe = grid[row][col]
    cons: set[Connections] = set()
    possible_cons = Connections.No
    mandatory_cons = Connections.No
    for con in grid[row][col].get_connections_for_all_orientations():
        dr, dc = COORDINATE_CHANGES[con]
        nr, nc = row+dr, col+dc
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue
        op_con = opposite_connection(con)
        if grid[nr][nc].char in CONNECTIONS_INDEX and op_con in grid[nr][nc].get_connections_for_all_orientations():
            if grid[nr][nc].final_orientation and not op_con in grid[nr][nc].connections:
                continue
            cons.add(con)
            possible_cons |= con
            if grid[nr][nc].final_orientation:
                mandatory_cons |= con
    possible: list[Pipe] = []
    for ori in pipe.get_orientations():
        if all(c in possible_cons for c in ori.connections):
            possible.append(ori)
    if len(possible) == 1:
        possible[0].final_orientation = True
    valid: list[Pipe] = []
    for pipe in possible:
        if all(c in pipe.connections for c in mandatory_cons):
            valid.append(pipe)
    if len(valid) == 1:
        valid[0].final_orientation = True
    return valid

def print_grid(grid: list[list[Pipe]]):
    for l in grid:
        print(''.join(x.char for x in l))

def solve(puzzle_input: str) -> int:
    data = [[Pipe(x) for x in d] for d in puzzle_input.encode().decode().splitlines()]

    def validate_grid(l: list[tuple[int,int]]):
        not_valid_yet: list[tuple[int,int]] = []
        for row, col in l:
            if len(v:=valid_orientations(data, row, col)) > 1:
                not_valid_yet.append((row,col))
            else:
                data[row][col] = v[0]
        return not_valid_yet

    print_grid(data)
    not_valid_yet: list[tuple[int,int]] = []
    start = (4,7) if "Start" in puzzle_input else (0,0)
    end = (19,72) if "Finish" in puzzle_input else (len(data)-1, len(data[0])-1)
    data[start[0]][start[1]].final_orientation = True
    data[end[0]][end[1]].final_orientation = True
    for row in range(start[0], end[0]+1):
        for col in range(start[1], end[1]+1):
            pipe = data[row][col]
            if pipe.char in CONNECTIONS_INDEX and not pipe.final_orientation:
                if len(v:=valid_orientations(data, row, col)) > 1:
                    not_valid_yet.append((row,col))
                else:
                    data[row][col] = v[0]
    while not_valid_yet:
        # print(f'rotations: {sum(c.rotations for r in data for c in r)}')
        # print_grid(data)
        not_valid_yet = validate_grid(not_valid_yet)
    print(f'rotations: {sum(c.rotations for r in data for c in r)}')
    print_grid(data)
    return sum(c.rotations for r in data for c in r)

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve, encoding="CP437")