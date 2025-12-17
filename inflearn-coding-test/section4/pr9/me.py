import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        current = arr[i][j]
        north = 0 if i - 1 < 0 else arr[i - 1][j]
        south = 0 if i + 1 >= N else arr[i + 1][j]
        west = 0 if j - 1 < 0 else arr[i][j - 1]
        east = 0 if j + 1 >= N else arr[i][j + 1]

        if current > north and current > south and current > west and current > east:
            cnt += 1

print(cnt)
