import sys

sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())

cnt = [0] * (n + m + 3)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

max_value = -2147000000
for i in range(n + m + 1):
    if cnt[i] > max_value:
        max_value = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max_value:
        print(i, end=' ')
