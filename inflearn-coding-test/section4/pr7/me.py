import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s=e=N//2


total = 0
for i in range(N):
    total += sum(arr[i][s:e + 1])

    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(total)
