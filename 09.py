from datetime import datetime
import os
from utils.runner import run_puzzle

def get_format_string(dates: list[str]):
    formats = {"%d-%m-%y": True, "%m-%d-%y": True, "%y-%m-%d": True, "%y-%d-%m": True}
    for date in dates:
        for fm in formats.keys():
            try:
                datetime.strptime(date, fm).date()
            except:
                formats[fm] = False
    return next(k for k,v, in formats.items() if v)

def solve(puzzle_input: str) -> str:
    data: dict[str, list[str]] = {}
    for line in puzzle_input.splitlines():
        date = line.split()[0][:-1]
        names = line[10:].split(', ')
        for name in names:
            if name in data:
                data[name].append(date)
            else:
                data[name] = [date]
    answer = []
    nineeleven = datetime(2001, 9, 11).date()
    for name, dates in data.items():
        formatstring = get_format_string(dates)
        for date in dates:
            if datetime.strptime(date, formatstring).date() == nineeleven:
                answer.append(name)
    answer.sort()
    return ' '.join(answer)

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)