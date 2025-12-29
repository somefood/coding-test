import timeit


def test_code():
    sum_ = 0
    for i in range(100_000_000):
        sum_ += 1

    print("Sum:", sum_)

execution_time = timeit.timeit(test_code, number=1)

print(f"Execution time in seconds: {execution_time:.6f}")
print(f"Execution time in milliseconds: {execution_time * 1_000:.3f}")
print(f"Execution time in nanoseconds: {execution_time * 1_000_000_000:.3f}")
