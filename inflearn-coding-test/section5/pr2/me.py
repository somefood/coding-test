import sys

sys.stdin = open("input.txt", "rt")


def get_total_count(mid):
    res = 0
    for a in arr:
        res += a // mid
    return res


K, N = map(int, input().split())

arr = [int(input()) for i in range(K)]

lt = 0
rt = max(arr)

res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    total = get_total_count(mid)

    if total >= N:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
