import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

result = a + b
result.sort()

print(result)
