def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                print(f"({arr[i]}, {arr[j]})")

arr = [2, 7, 4, 9, 1]
target = 10
two_sum(arr, target)