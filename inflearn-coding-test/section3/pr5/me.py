import sys

sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())

results = [0 for i in range(N + M + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
       total = i + j
       results[total] = results[total] + 1

max_value = max(results)

for i in range(1, len(results)):
    if results[i] == max_value:
        print(i, end=' ')

