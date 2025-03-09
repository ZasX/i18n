from collections import Counter
import os
import time
from dateutil import parser
from utils.runner import run_puzzle

def solve(puzzle_input: list[str]):
    epochs = []
    for line in puzzle_input:
        DT = parser.parse(line)
        epochs.append(int(DT.timestamp()))
    epoch = next(epoch for epoch, cnt in Counter(epochs).items() if cnt == 4)
    return time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(epoch))+'+00:00'

if __name__ == "__main__":
    # Dynamically detect day number from filename
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)