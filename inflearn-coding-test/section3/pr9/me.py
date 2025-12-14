import sys
from typing import List

sys.stdin = open("input.txt", "rt")

N = int(input())

inputs = []


def calculate(s: List[int]) -> int:
    if s[0] == s[1] and s[1] == s[2]:
        return 10000 + s[0] * 1000
    else:
        if s[0] == s[1]:
            return 1000 + s[0] * 100
        elif s[1] == s[2]:
            return 1000 + s[1] * 100
        elif s[0] == s[2]:
            return 1000 + s[0] * 100
    return max(s) * 100

results = []
for i in range(N):
    s = list(map(int, input().split()))
    results.append(calculate(s))

print(max(results))
