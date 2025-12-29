'''
hashmap 이용 O(n)
'''

def twoSum(nums, target):
    seen = {}  # 비어있는 hashmap 선언

    for i, v in enumerate(nums):
        complement = target - v
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[v] = i

    return False
