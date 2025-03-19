import unicodedata
from utils.runner import run_puzzle
import os
from functools import cmp_to_key
import locale
import re

def solve(puzzle_input: str) -> int:
    data = {unicodedata.normalize('NFKD', line.split(': ')[0].replace(',', '~')):int(line.split(': ')[1]) for line in puzzle_input.splitlines()}
    bla = {e:[ord(x) for x in e] for e in data.keys()}

    locale.setlocale(locale.LC_COLLATE, 'en_US.UTF-8')
    o1 = sorted(data.keys(), key=cmp_to_key(locale.strcoll))

    locale.setlocale(locale.LC_COLLATE, 'sv_SE.UTF-8')
    o2 = sorted(data.keys(), key=cmp_to_key(locale.strcoll))

    locale.setlocale(locale.LC_COLLATE, 'nl_NL.UTF-8')
    l3 = [re.sub(r"^[^A-Z]*([A-Z].*)", r"\1", name) for name in data.keys()]
    o3 = sorted(l3, key=cmp_to_key(locale.strcoll))

    return data[o1[len(o1)//2]]*data[o2[len(o2)//2]]*data[o3[len(o3)//2]]

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)