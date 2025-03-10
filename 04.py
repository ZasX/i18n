import os
from utils.runner import run_puzzle
from dateutil import parser, tz
from datetime import datetime, time

def parse_line(line: str):
    l = line.split()
    default_date = datetime.combine(datetime.now(),
                                time(0, tzinfo=tz.gettz(l[1])))
    dt = parser.parse(' '.join(l[2:]), default=default_date)
    return dt

def solve(puzzle_input: list[str]) -> int:
    total_minutes = 0
    for i in range(0, len(puzzle_input), 3):
        departure = parse_line(puzzle_input[i])
        arrival = parse_line(puzzle_input[i+1])
        total_minutes += (arrival-departure).seconds//60
    return total_minutes

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)