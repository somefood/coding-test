import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

i = 0

cnt = 0
while i < N:
    j = i
    while j < N:
        if sum(arr[i:j+1]) == M:
            cnt += 1
        j += 1
    i += 1


print(cnt)
