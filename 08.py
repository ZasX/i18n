import os
from utils.runner import run_puzzle
from unidecode import unidecode
from collections import Counter

def solve(puzzle_input: str) -> int:
    valid = 0
    vowels= ('a', 'e', 'i', 'o', 'u')
    for line in [line.strip() for line in puzzle_input.splitlines()]:
        if len(line) < 4 or len(line) > 12: continue
        if not any(c.isnumeric() for c in line): continue
        no_special_chars_line = unidecode(line).lower()
        if not any(c in vowels for c in no_special_chars_line): continue
        if not any(c for c in no_special_chars_line if c.isalpha() and c not in vowels): continue
        if any(cnt > 1 for cnt in Counter(no_special_chars_line).values()): continue
        valid += 1
    return valid

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)