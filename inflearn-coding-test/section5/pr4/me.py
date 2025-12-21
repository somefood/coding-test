import sys

sys.stdin = open("input.txt", "rt")


def count(length):
    cnt = 1
    ep = arr[0]
    for i in range(1, N):
        if arr[i] - ep >= length:
            cnt += 1
            ep = arr[i]
    return cnt


N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

lt = 1
rt = max(arr)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= C:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
