"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
    1 <= nums.length <= 3 * 10**4
    -2**31 <= nums[i] <= 2**31 - 1
    Each element in nums appears exactly three times except for one element which appears once.
"""
from typing import List


def single_number(nums: List[int]) -> int:
    ones: int = 0
    twos: int = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


if __name__ == '__main__':
    assert single_number([2, 2, 3, 2]) == 3
    assert single_number([0, 1, 0, 1, 0, 1, 99])