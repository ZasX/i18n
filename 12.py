from utils.runner import run_puzzle
import os
from functools import cmp_to_key
import locale
import re

def solve(puzzle_input: str) -> int:
    data = {line.split(': ')[0]:int(line.split(': ')[1]) for line in puzzle_input.splitlines()}

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    o1 = sorted(data.keys(), key=cmp_to_key(locale.strcoll))

    locale.setlocale(locale.LC_ALL, 'se_NO.UTF-8')
    o2 = sorted(data.keys(), key=cmp_to_key(locale.strcoll))

    locale.setlocale(locale.LC_ALL, 'nl_NL.UTF-8')
    l3 = [re.sub(r"^[^A-Z]*([A-Z].*)", r"\1", name) for name in data.keys()]
    o3 = sorted(l3, key=cmp_to_key(locale.strcoll))

    return data[o1[len(o1)//2]]*data[o2[len(o2)//2]]*data[o3[len(o3)//2]]

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)