import sys
sys.stdin = open("input.txt", "rt")

N = 10

arr = [i for i in range(21)]

for _ in range(N):
    a, b = map(int, input().split())
    slice_arr = arr[a:b + 1]
    arr[a:b+1] = slice_arr[::-1]

print(arr[1:])



