import os
from utils.runner import run_puzzle

def solve(puzzle_input: str) -> int:
    words, crossword = [lines.splitlines() for lines in puzzle_input.split('\n\n')]
    for i, word in enumerate(words, 1):
        if i%3 == 0 or i%5 == 0:
            word = bytes(word, 'iso-8859-1').decode('utf-8')
        if i%3 == 0 and i%5 == 0:
            word = bytes(word, 'iso-8859-1').decode('utf-8')
        words[i-1] = word
    solution = 0
    for line in (l.strip() for l in crossword):
        ci, c = next((i, l) for i, l in enumerate(line) if l != '.')
        word_index = next(i for i, word in enumerate(words) if len(word) == len(line) and word[ci] == c)+1
        solution += word_index
    return solution

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)