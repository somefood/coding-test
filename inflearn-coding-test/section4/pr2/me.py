import sys
sys.stdin = open("input.txt", "rt")

a = input()

result = ""
for i in a:
    if i.isnumeric():
        result += i

result = int(result)

cnt = 0
for i in range(1, result+1):
    if result % i == 0:
        cnt += 1


print(result)
print(cnt)
