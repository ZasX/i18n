from collections import namedtuple
import os
from datetime import datetime, timedelta
from dateutil import parser
from calendar import monthrange
from zoneinfo import ZoneInfo
from utils.runner import run_puzzle

class support245:
    def __init__(self, s: str) -> None:
        # The first section is a list of support offices, the time zone where they are located, and a list of public holidays
        splat = s.split('\t')
        self.name = ''.join(splat[0].split()[3:]) if splat[0].startswith('TOPlap') else splat[0]
        self.tz = ZoneInfo(splat[1])
        self.hollidays = [parser.parse(x) for x in splat[2].split(';')]
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.tz}"

Date = namedtuple("Date", ["year", "month", "day"])

def all_dates_in_year(year=2022):
    for month in range(1, 13): # Month is always 1..12
        for day in range(1, monthrange(year, month)[1] + 1):
            yield Date(year, month, day)

def solve(puzzle_input: str) -> int:
    support_offices, customer_companies = [[support245(y) for y in x.splitlines()] for x in puzzle_input.split('\n\n')]
    for date in all_dates_in_year():
        ...
    return 0

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)