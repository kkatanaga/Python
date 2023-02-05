def twoSum(nums, target):
    last = len(nums)
    for i, x in enumerate(nums):
        for j, y in enumerate(nums[i+1:last]):
            if x + y == target:
                return [i, i + j + 1]
    return None

print(twoSum([11, 2, 15, 17, 16], 9))