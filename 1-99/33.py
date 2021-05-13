"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

Constraints:
    1 <= nums.length <= 5000
    -10**4 <= nums[i] <= 10**4
    All values of nums are unique.
    nums is guaranteed to be rotated at some pivot.
    -10**4 <= target <= 10**4
"""
from typing import List


def get_pivot_point(nums: List[int]) -> int:
    left: int = 0
    right: int = len(nums) - 1

    while left < right:
        mid: int = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


def search(nums: List[int], target: int) -> int:
    pivot: int = get_pivot_point(nums)
    left: int = 0
    right: int = len(nums) - 1

    if nums[pivot] <= target <= nums[right]:
        left = pivot
    else:
        right = pivot

    while left <= right:
        mid: int = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
