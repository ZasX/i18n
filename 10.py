from functools import lru_cache
from itertools import product
import os
import unicodedata
from utils.runner import run_puzzle
import bcrypt

@lru_cache(None)
def forms(s: str):
    a = []
    s = unicodedata.normalize("NFC", s)
    for l in s:
        la = []
        la.append(l.encode())
        la.append(unicodedata.normalize("NFD", l).encode())
        a.append(set(la))
    return set([b''.join(combination) for combination in product(*a)])

def solve(puzzle_input: str) -> int:

    # I'm leaving my trial and error code in, because it's quite a lot today:

    # pwattempt  = ".pM?XÑ0i7ÈÌ"
    # pworiginal = ".pM?XÑ0i7ÈÌ"

    # for pw in forms(pwattempt):
    #     if pw == pworiginal.encode():
    #         ...

    # pwaf = forms(pwattempt)
    # pwof = forms(pworiginal)
    # for pw1 in pwaf:
    #     for pw2 in pwof:
    #         # print(pw.encode())
    #         # print(pw2.encode())
    #         # print('---')
    #         if pw1 == pw2:
    #             print(pw1)
    #             print(pw2)
    #             print('---')
    #             print(pwattempt.encode())
    #             print(pworiginal.encode())
    #             print('-----')
    #             ...

    # print(unicodedata.normalize("NFC", pwattempt) == unicodedata.normalize("NFC", pworiginal))
    # print(unicodedata.normalize("NFKC", pwattempt) == unicodedata.normalize("NFKC", pworiginal))
    # print(unicodedata.normalize("NFD", pwattempt) == unicodedata.normalize("NFD", pworiginal))
    # print(unicodedata.normalize("NFKD", pwattempt) == unicodedata.normalize("NFKD", pworiginal))
    # unicodedata.normalize("NFKC", pwattempt)
    # unicodedata.normalize("NFD", pwattempt)
    # unicodedata.normalize("NFKD", pwattempt)

    # pw1u = unidecode(pwattempt)
    # pw2u = unidecode(pworiginal)

    # pw1b = bcrypt.checkpw(pwattempt.encode(), "$2b$07$0EBrxS4iHy/aHAhqbX/ao.n7305WlMoEpHd42aGKsG21wlktUQtNu".encode())
    # pw2b = bcrypt.checkpw(pworiginal.encode(), "$2b$07$0EBrxS4iHy/aHAhqbX/ao.n7305WlMoEpHd42aGKsG21wlktUQtNu".encode())

    # test = "test"
    # test2 = "test2"
    # salt = bcrypt.gensalt()
    # p1 = bcrypt.hashpw(test.encode(), salt)
    # p2 = bcrypt.hashpw(test2.encode(), salt)
    
    passwords, attempts = puzzle_input.split('\n\n')
    pwdsoriginal: dict[str, bytes] = {}
    for password in passwords.splitlines():
        splat = password.split()
        pwdsoriginal[splat[0]] = splat[1].encode()
    count = 0
    for attempt in attempts.splitlines():
        splat = attempt.split()
        for pwinput in forms(splat[1]):
            if bcrypt.checkpw(pwinput, pwdsoriginal[splat[0]]):
                count += 1
                break
    return count

if __name__ == "__main__":
    day = os.path.splitext(os.path.basename(__file__))[0]
    run_puzzle(day, solve)