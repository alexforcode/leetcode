"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

Constraints:
    1 <= nums.length <= 10**4
    -9999 <= nums[i], target <= 9999
    All the integers in nums are unique.
    nums is sorted in an ascending order.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    start: int = 0
    end: int = len(nums) - 1

    while start <= end:
        mid: int = start + (end - start) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
