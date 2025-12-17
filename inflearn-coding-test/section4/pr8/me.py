import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

M = int(input())

for i in range(M):
    h, t, k = map(int, input().split())

    for _ in range(k):
        if t == 0:
            a[h - 1].append(a[h - 1].pop(0))
        else:
            a[h - 1].insert(0, a[h - 1].pop())


total = 0
s = 0
e = N - 1

for i in range(N):
    for j in range(s, e + 1):
        total += a[i][j]
    if i < N // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(total)
