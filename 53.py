"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Constraints:
    1 <= nums.length <= 3 * 104
    -105 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    max_sum: int = nums[0]
    cur_sum: int = max_sum

    for idx in range(1, len(nums)):
        cur_sum = max(nums[idx] + cur_sum, nums[idx])
        max_sum = max(cur_sum, max_sum)

    return max_sum


if __name__ == '__main__':
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
