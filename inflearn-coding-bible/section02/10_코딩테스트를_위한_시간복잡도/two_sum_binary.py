def two_sum(nums, target):
    nums.sort()

    l, r = 0, len(nums) - 1

    while l < r:
        if target > nums[l] + nums[r] : l += 1
        elif target < nums[l] + nums[r] : r -= 1
        else: return True
    return False
