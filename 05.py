import os
from utils.runner import run_puzzle

def solve(puzzle_input: str) -> int:
    pos = 0
    count = 0
    for line in [line.strip('\n') for line in puzzle_input.splitlines()]:
        if line[pos] == "💩":
            count += 1
        pos = (pos+2)%len(line)
    return count

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)