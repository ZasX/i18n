import codecs
import os
from utils.runner import run_puzzle

def decode_word(b: bytes):
    r = ''
    try:
        word = b.decode('latin-1')
        if not any([not c.isalpha() for c in word]):
            r = word
    except:
        ...
    if not r:
        try:
            word = (b[len(codecs.BOM_UTF8):] if b.startswith(codecs.BOM_UTF8) else b).decode('UTF-8')
            if not any([not c.isalpha() for c in word]):
                r = word
        except:
            ...
    if not r:
        try:
            word = (b[len(codecs.BOM_UTF16_LE):] if b.startswith(codecs.BOM_UTF16_LE) else b).decode('UTF-16LE')
            if not any([not c.isalpha() for c in word]) and max(ord(c) for c in word) < 256:
                r = word
        except:
            ...
    if not r:
        try:
            word = (b[len(codecs.BOM_UTF16_BE):] if b.startswith(codecs.BOM_UTF16_BE) else b).decode('UTF-16BE')
            if not any([not c.isalpha() for c in word]):
                r = word
        except:
            ...
    return r

def solve(puzzle_input: str) -> int:
    words, puzzle = puzzle_input.split('\n\n')
    words = [decode_word(bytes.fromhex(line)) for line in words.splitlines()]
    puzzle = [line.strip() for line in puzzle.splitlines()]
    char_indices: dict[str, list] = {}
    for row_index, row in enumerate(puzzle):
        for col_index, char in enumerate(row):
            if char != '.':
                if char not in char_indices:
                    char_indices[char] = []
                char_indices[char].append((col_index, len(row), row_index))
    sum_row_nr = 0
    for i, word in enumerate(words, 1):
        for j, char in enumerate(word):
            if char in char_indices:
                for ind in char_indices[char]:
                    if j == ind[0] and len(word) == ind[1]:
                        sum_row_nr += i
    return sum_row_nr

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)