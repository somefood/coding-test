import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max_value = 0
# 대각선 1
total = 0
for i in range(N):
    total += arr[i][i]
if total > max_value:
    max_value = total

# 대각선 2
total = 0
for i in range(N):
    total += arr[i][N - 1 - i]
if total > max_value:
    max_value = total

# 가로
for i in range(N):
    total = 0
    for j in range(N):
        total += arr[i][j]
    if total > max_value:
        max_value = total

# 세로
for i in range(N):
    total = 0
    for j in range(N):
        total += arr[j][i]
    if total > max_value:
        max_value = total

print(max_value)
