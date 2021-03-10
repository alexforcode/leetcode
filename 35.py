"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Constraints:
    1 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    nums contains distinct values sorted in ascending order.
    -10**4 <= target <= 10**4
"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    low: int = 0
    high: int = len(nums) - 1

    while low <= high:
        mid: int = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == '__main__':
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 0) == 0
