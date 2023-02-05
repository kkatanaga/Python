from math import ceil

def findMedianSortedArrays(nums1, nums2):
    num1 = 0
    nums1_max = len(nums1)
    num2 = 0
    nums2_max = len(nums2)
    nums3 = []
    num3 = 0
    
    while num1 < nums1_max or num2 < nums2_max:
        if num1 == nums1_max:
            nums3.append(nums2[num2])
            num2 += 1
        elif num2 == nums2_max:
            nums3.append(nums1[num1])
            num1 += 1
        elif nums1[num1] < nums2[num2]:
            nums3.append(nums1[num1])
            num1 += 1
        else:
            nums3.append(nums2[num2])
            num2 += 1
        num3 += 1
    
    median = 0.0
    median_index = int(num3 / 2)
    
    if num3 % 2 != 0:
        median = float(nums3[median_index])
    else:
        median = (nums3[median_index - 1] + ceil(nums3[median_index])) / 2.0
    
    return median

result = findMedianSortedArrays([1], [])
print(result)
result = findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25])
print(result)
result = findMedianSortedArrays([23, 26, 31, 35], [3, 5, 7, 9, 11, 16])
print(result)
result = findMedianSortedArrays([3, 5, 7, 9], [23, 26, 31, 35, 37, 42]) # 3, 5, 7, 9, 23, 26, 31, 35, 37, 42
print(result)