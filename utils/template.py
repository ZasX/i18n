import os
from utils.runner import run_puzzle

def solve(puzzle_input: str) -> int:
    # TODO: Your logic here
    return 0

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)