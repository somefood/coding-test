import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
tmp = list(map(int, input().split()))

results = []
for i in range(N):
    if i == 0:
        results.append(tmp[i])
        continue

    if tmp[i] == 0:
        results.append(tmp[i])
    else:
        results.append(results[i - 1] + 1)

print(sum(results))
