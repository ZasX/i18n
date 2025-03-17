import os
import time
import unicodedata
import bcrypt
from collections import Counter
from itertools import product
from multiprocessing.dummy import Pool
from utils.runner import run_puzzle

def generate_variants(text: str) -> set[bytes]:
    """Generate all possible Unicode normalization variants of a string."""
    normalized_text = unicodedata.normalize("NFC", text)
    variants = []
    
    for char in normalized_text:
        char_variants = {char.encode(), unicodedata.normalize("NFD", char).encode()}
        variants.append(char_variants)
    
    return {b"".join(combination) for combination in product(*variants)}

def verify_attempt(attempt_data: tuple[str, int], stored_passwords: dict[str, bytes]) -> int:
    """Check if an attempt matches any stored password and return the count if it does."""
    attempt, count = attempt_data
    user, entered_password = attempt.split()
    
    for variant in generate_variants(entered_password):
        if bcrypt.checkpw(variant, stored_passwords[user]):
            return count
    return 0

def solve(puzzle_input: str) -> int:
    """Solve the puzzle by verifying password attempts."""
    password_data, attempt_list = puzzle_input.split('\n\n')
    passwords = dict(line.split() for line in password_data.splitlines())
    stored_passwords = {user: hashed.encode() for user, hashed in passwords.items()}
    attempts = Counter(attempt_list.splitlines()).items()
    
    with Pool(32) as pool:
        results = pool.starmap(verify_attempt, [(attempt, stored_passwords) for attempt in attempts])
    
    return sum(results)

if __name__ == "__main__":
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    start_time = time.time()
    run_puzzle(script_name, solve)
    print(f"Execution time: {time.time() - start_time:.4f} seconds")
