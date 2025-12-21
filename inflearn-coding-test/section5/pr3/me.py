import sys

sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = list(map(int, input().split()))

lt = 1
rt = sum(arr)
maxx = max(arr)

res = 0


def count(capacity):
    cnt = 1
    total = 0
    for x in arr:
        if x + total > capacity:
            cnt += 1
            total = x
        else:
            total += x

    return cnt


while lt <= rt:
    mid = (lt + rt) // 2

    if mid >= maxx and count(mid) <= M:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
