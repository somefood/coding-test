import math
import sys

sys.stdin = open("input.txt", "rt")


def reverse(x: int) -> int:
    return int(str(x)[::-1])


def is_prime(x: int) -> bool:
    # 예외 처리
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:  # 짝수 제외
        return False

    # 홀수만 확인 (2배 더 빠름)
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


n = int(input())
inputs = list(map(int, input().split()))

for i in inputs:
    reversed_value = reverse(i)
    if is_prime(reversed_value):
        print(reversed_value, end=' ')
