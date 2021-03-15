"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such
that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

Constraints:
    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    nums is guaranteed to be rotated at some pivot.
    -104 <= target <= 104
"""
from typing import List


def search(nums: List[int], target: int) -> bool:
    start: int = 0
    end: int = len(nums) - 1

    while start <= end:
        mid: int = start + (end - start) // 2

        if nums[mid] == target:
            return True

        if nums[start] == nums[mid] == nums[end]:
            start += 1
            end -= 1
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return False


if __name__ == '__main__':
    assert search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert search([3, 4, 5, 2, 2, ], 3) is True
    assert search([1, 1, 1, 1, 1, 2, 1, 1, 1], 2) is True
    assert search([1, 0, 1, 1, 1], 0) is True

