import sys
sys.stdin = open('input.txt', 'rt')

def digit_sum(x: str) -> int:
    total = 0
    for a in x:
        total += int(a)
    return total

n = int(input())
inputs = list(input().split())

print(max(inputs, key=digit_sum))
