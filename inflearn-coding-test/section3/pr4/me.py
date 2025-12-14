import sys
import math

def get_sign(num):
    if num >= 0:
        return True
    else:
        return False

sys.stdin = open('input.txt', 'rt')

N = int(input())
inputs = list(map(int, input().split()))

total = sum(inputs)
average = math.ceil(total / N)

# print(total, average)

results = []
for i in inputs:
    results.append(i - average)

results = list(map(lambda x: (abs(x), get_sign(x)), results))
# print(results)

minValue = min(results, key = lambda x: x[0])[0]
# print(minValue)

print(average, results.index((minValue, True)) + 1)
