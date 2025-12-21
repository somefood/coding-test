import sys
sys.stdin = open("input.txt", "rt")

def count(capacity):
    cnt = 1
    total = 0
    for x in music:
        if total + x > capacity:
            cnt += 1
            total = x
        else:
            total += x
    return cnt

n, m = map(int, input().split())
music = list(map(int, input().split()))

lt = 1
rt = sum(music)

res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) <= m: # 그 이하가 되었다면 m은 무조건 됨
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
