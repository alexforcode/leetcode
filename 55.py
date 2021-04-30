"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Constraints:
    1 <= nums.length <= 3 * 10**4
    0 <= nums[i] <= 10**5
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    max_idx: int = 0

    for idx, val in enumerate(nums):
        if idx > max_idx:
            return False

        max_idx = max(max_idx, idx + val)

    return True


if __name__ == '__main__':
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
