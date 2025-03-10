import os
from utils.runner import run_puzzle

def solve(puzzle_input: list[str]) -> int:
    valid = 0
    for line in puzzle_input:
        if len(line) < 4 or len(line) > 12: continue
        if not any(c.isnumeric() for c in line): continue
        if not any(c.isupper() for c in line): continue
        if not any(c.islower() for c in line): continue
        if not any(ord(c) > 127 for c in line): continue
        valid += 1
    return valid

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)