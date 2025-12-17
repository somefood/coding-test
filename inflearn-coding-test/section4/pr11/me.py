import sys

sys.stdin = open("input.txt", "rt")

N = 7

arr = [list(map(int, input().split())) for i in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if (
                i - 1 < 0 or i - 2 < 0 or
                j - 1 < 0 or j - 2 < 0 or
                i + 1 > N or i + 2 > N or
                j + 1 > N or j + 2 > N
        ):
            continue

        if arr[i][j-1] == arr[i][j+1] and arr[i][j-2] == arr[i][j+2]:
            cnt += 1
        if arr[j - 1][i] == arr[j + 1][i] and arr[j - 2][i] == arr[j + 2][i]:
            cnt += 1

print(cnt)

