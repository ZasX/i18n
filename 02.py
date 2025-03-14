from collections import Counter
import os
import time
from dateutil import parser
from utils.runner import run_puzzle

def solve(puzzle_input: str):
    epochs = []
    for line in [line.strip() for line in puzzle_input.splitlines()]:
        dt = parser.parse(line)
        epochs.append(int(dt.timestamp()))
    epoch = next(epoch for epoch, cnt in Counter(epochs).items() if cnt == 4)
    return time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(epoch))+'+00:00'

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)