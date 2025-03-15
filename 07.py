import datetime
from dateutil import parser
import pytz
import os
from utils.runner import run_puzzle

def is_dst(dt: datetime.datetime):
   return dt.dst() != datetime.timedelta(0,0)

def solve(puzzle_input: str) -> int:
    data = [(parser.parse(v1), int(v2), int(v3)) for v1, v2, v3 in [line.split() for line in puzzle_input.splitlines()]]
    halifax = pytz.timezone("America/Halifax")
    santiago = pytz.timezone("America/Santiago")
    answer = 0
    i = 1
    for date, correct, wrong in data:
        # -4:00 offset indicates Halifax in northern winter
        dutc = date.astimezone(datetime.timezone.utc)
        dhal = dutc.astimezone(halifax)
        dsan = dutc.astimezone(santiago)
        if date.tzinfo and (offset := date.tzinfo.utcoffset(date)) and offset.seconds == 75600: # -3
            if not is_dst(dhal):
                # southern winter
                answer += i * (dutc + datetime.timedelta(minutes=(correct-wrong))).astimezone(santiago).hour
            else:
                # southern summer
                answer += i * (dutc + datetime.timedelta(minutes=(correct-wrong))).astimezone(halifax).hour
        else: # -4
            if is_dst(dhal):
                # southern summer
                answer += i * (dutc + datetime.timedelta(minutes=(correct-wrong))).astimezone(santiago).hour
            else:
                # northern winter
                answer += i * (dutc + datetime.timedelta(minutes=(correct-wrong))).astimezone(halifax).hour
        i += 1
    return answer

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)