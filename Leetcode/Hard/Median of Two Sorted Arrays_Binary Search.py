# Explanation: https://www.youtube.com/watch?v=LPFhl65R7ww

from math import ceil

def findMedianSortedArrays(nums1, nums2):
    # Make sure the length of nums1 < length of nums2
    nums1_len = len(nums1)
    nums2_len = len(nums2)

    if nums2_len < nums1_len:
        return findMedianSortedArrays(nums2, nums1)

    # Binary Search
    start = 0
    end = nums1_len

    while True:
        num1_partition_index = int((start + end) / 2)
        num2_partition_index = int((nums1_len + nums2_len + 1) / 2) - num1_partition_index
        
        l1 = -999999999999 if num1_partition_index == 0 else nums1[num1_partition_index - 1]
        r1 = 999999999999 if num1_partition_index == nums1_len else nums1[num1_partition_index]

        l2 = -999999999999 if num2_partition_index == 0 else nums2[num2_partition_index - 1]
        r2 = 999999999999 if num2_partition_index == nums2_len else nums2[num2_partition_index]

        if l1 <= r2 and l2 <= r1:
            break
        elif l1 > r2:
            end = num1_partition_index - 1
        else:
            start = num1_partition_index + 1
    
    # Find the Median
    if (nums1_len + nums2_len) % 2 == 0:
        return (max(l1, l2) + min(r1, r2)) / 2.0
    else:
        return float(max(l1, l2))

result = findMedianSortedArrays([1], [])
print(result)
result = findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25])
print(result)
result = findMedianSortedArrays([23, 26, 31, 35], [3, 5, 7, 9, 11, 16])
print(result)
result = findMedianSortedArrays([3, 5, 7, 9], [23, 26, 31, 35, 37, 42]) # 3, 5, 7, 9, 23, 26, 31, 35, 37, 42
print(result)