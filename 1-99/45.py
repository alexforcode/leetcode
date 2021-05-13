"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 10**5
"""
from typing import List


def jump(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    start: int = 0
    end: int = 0
    max_idx: int = 0
    steps: int = 1

    while True:
        for idx in range(start, end+1):
            max_idx = max(max_idx, idx + nums[idx])

        if max_idx >= len(nums) - 1:
            return steps

        steps += 1
        start = end + 1
        end = max_idx


if __name__ == '__main__':
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
