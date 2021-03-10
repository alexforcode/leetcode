"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Constraints:
    0 <= nums.length <= 10**5
    -10**9 <= nums[i] <= 10**9
    nums is a non-decreasing array.
    -10**9 <= target <= 10**9
"""
from typing import List


def get_boundary(nums: List[int], target: int, left: bool) -> int:
    index: int = -1
    start: int = 0
    end: int = len(nums) - 1

    while start <= end:
        mid: int = start + (end - start) // 2
        if nums[mid] == target:
            index = mid

        if left:
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

    return index


def search_range(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    left_index: int = get_boundary(nums, target, True)
    right_index: int = get_boundary(nums, target, False)

    return [left_index, right_index]


if __name__ == '__main__':
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
