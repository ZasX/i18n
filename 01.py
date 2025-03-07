import os
from utils.runner import run_puzzle

def solve(puzzle_input: list[str]) -> int:
    max_bytes = 160
    max_chars = 140
    cost_sms_tweet_both = (11,7,13)
    total_cost = 0
    for line in puzzle_input:
        byte_length = len(line.encode('utf-8'))
        num_of_chars = len(line)
        line_cost = 0
        if byte_length <= max_bytes:
            line_cost += cost_sms_tweet_both[0]
        if num_of_chars <= max_chars:
            line_cost += cost_sms_tweet_both[1]
        total_cost += line_cost if line_cost <= 13 else 13
    return total_cost

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)
