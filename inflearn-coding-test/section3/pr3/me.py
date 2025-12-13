import sys
from itertools import permutations, combinations_with_replacement

sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
inputs = map(int, input().split())

results = []
for i in permutations(inputs, 3):
    results.append(sum(i))

results = list(set(results))
results.sort(reverse=True)
print(results[K - 1])

