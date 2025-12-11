import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: # for 문이 정상적으로 끝난 경우, k 번째 약수가 없음
    print(-1)
