from typing import Any


import os
import japanese_numbers
from utils.runner import run_puzzle

JAPANESE_UNITS = {'間':6*10000, '丈':10*10000, '町':360*10000, '里':12960*10000, '毛': 1, '厘': 10, '分': 100, '寸': 1000}
# 1 Shaku (尺) = 10/33 m

# The Japanese system also knows larger units:

# 1 Ken (間) = 6 Shaku (尺)
# 1 Jo (丈) = 10 Shaku (尺)
# 1 Cho (町) = 360 Shaku (尺)
# 1 Ri (里) = 12960 Shaku (尺)

# As well as smaller units:

# 10,000 Mo (毛) = 1 Shaku (尺)
# 1000 Rin (厘) = 1 Shaku (尺)
# 100 Bu (分) = 1 Shaku (尺)
# 10 Sun (寸) = 1 Shaku (尺)
def convert_number(n:int, u:str):
    if u in JAPANESE_UNITS:
        return n*JAPANESE_UNITS[u]
    return n*10000

def solve(puzzle_input: str) -> int:
    numbers = [[(japanese_numbers.to_arabic(v), v[-1]) for v in n.split(' × ')] for n in puzzle_input.splitlines()]
    total = 0
    for n1, n2 in numbers:
        new1, new2 = convert_number(n1[0][0].number, n1[1]), convert_number(n2[0][0].number, n2[1])
        sm = ((new1*new2)*(10*10)//(33*33))//(10000*10000)
        print(n1[0][0].number, n2[0][0].number, sm)
        total += sm
    return total

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)