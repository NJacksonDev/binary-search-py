# [ 1, 7, 10, 15, 30, 40]
# [7]


# Use a binary search for a sorted list
# Divide the original list in two - divide the length of the list by 2
# Can cut the list in half and only focus on one half by determining if the mid-point's value is higher or lower than the target value
# formula to calculate mid-point = add the high and low indices (e.g., 0 + 5 in the list above) and // (floor division - rounds down) by 2



from typing import List
# without typing function looks like this: def serach(nums, target):
def search(nums: List[int], target: int) -> int:
    length = len(nums) -1
    low, high = 0, length

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(search([1, 7, 10, 15, 30, 40], 7))