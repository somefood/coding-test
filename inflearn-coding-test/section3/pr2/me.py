T = int(input())

results = []
for _ in range(T):
    n, s, e, k = map(int, input().split())
    inputs = list(map(int, input().split()))

    inputs = inputs[s-1:e]
    l = sorted(inputs)
    results.append(l[k - 1])

for index, r in enumerate(results):
    print(f"#{index} {r}")


