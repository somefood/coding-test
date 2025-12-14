import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    tot = 0
    while x > 0:
        tot += x % 10
        x = x // 10
    return tot

def digit_sum2(x):
    tot = 0
    for i in str(x):
        tot += int(i)
    return tot

max_value = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max_value:
        max_value = tot
        res = x

print(res)
