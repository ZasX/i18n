import os
from utils.runner import run_puzzle

def solve(puzzle_input: list[str]) -> int:
    # TODO: Your logic here
    return 0

if __name__ == "__main__":
    # Dynamically detect day number from filename
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)