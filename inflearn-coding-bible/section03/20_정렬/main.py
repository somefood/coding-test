nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)

nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)
print(sorted_nums)
print(nums)

text = "cdbae"

text_list = list(text)
text_list.sort()
sorted_text = "".join(text_list)

print(sorted_text)

text = "cdbae"

sorted_text = "".join(sorted(text))
print(sorted_text)

nums = [3, 1, 4, 1, 5]
nums.sort(reverse=True)
print(nums)

data = ["apple", "banana", "kiwi"]
data.sort(key=len)
print("sort():", data)

data = ["apple", "banana", "kiwi"]
sorted_data = sorted(data, key=len)
print("sorted():", sorted_data)

data = ["apple", "banana", "kiwi"]
data.sort(key=len, reverse=True)
print("sort(reverse=True):)", data)

data = ["apple", "banana", "kiwi"]
sorted_data = sorted(data, key=len, reverse=True)
print("sorted(reverse=True):", sorted_data)

def get_second_element(item):
    return item[1]

data = [("apple", 3), ("banana", 1), ("cherry", 2)]
data.sort(key=get_second_element)
print("sort()", data)

# sorted()로 정렬
data = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_data = sorted(data, key=get_second_element)  # 새 리스트 반환
print("sorted():", sorted_data)  # 결과: [('banana', 1), ('cherry', 2), ('apple', 3)]

data = [("apple", 3), ("banana", 1), ("cherry", 2)]
data.sort(key=lambda x: x[1])
print("sort()", data)

data = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print("sorted():", sorted_data)