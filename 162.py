"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Constraints:
    1 <= nums.length <= 1000
    -2**31 <= nums[i] <= 2**31 - 1
    nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


def find_peak_element(nums: List[int]) -> int:
    start: int = 0
    end: int = len(nums) - 1

    while start < end:
        mid: int = start + (end - start) // 2
        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid + 1

    return start


if __name__ == '__main__':
    assert find_peak_element([1, 2, 3, 1]) == 2
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) == 5
    assert find_peak_element([2]) == 0
