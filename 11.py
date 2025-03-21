import os
from utils.runner import run_puzzle

UPPERGREEK = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
LOWERGREEK = "αβγδεζηθικλμνξοπρστυφχψω"
ODYSEUS = ("Οδυσσευσ","Οδυσσεωσ","Οδυσσει","Οδυσσεα","Οδυσσευ")

def rotate(s: str, p: int):
    result = ""
    for c in s:
        if c in UPPERGREEK:
            i = UPPERGREEK.index(c)
            result += UPPERGREEK[(i+p)%len(UPPERGREEK)]
        elif c in LOWERGREEK:
            i = LOWERGREEK.index(c)
            result += LOWERGREEK[(i+p)%len(LOWERGREEK)]
        else:
            result += c
    return result

def odyseus_in_rot(line: str):
    for i in range(24):
        newline = rotate(line, i)
        for o in ODYSEUS:
            if o in newline:
                return i
    return 0

def solve(puzzle_input: str) -> int:
    answer = 0
    puzzle_input = puzzle_input.replace('ς', 'σ')
    for line in puzzle_input.splitlines():
        answer += odyseus_in_rot(line)
    return answer

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)