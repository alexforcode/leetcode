"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money
you can rob tonight without alerting the police.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    loot1: int = 0
    prev: int = 0

    for num in nums[1:]:
        loot1, prev = max(num + prev, loot1), loot1

    nums[-1] = 0
    loot2: int = 0
    prev = 0

    for num in nums:
        loot2, prev = max(num + prev, loot2), loot2

    return max(loot1, loot2)


if __name__ == '__main__':
    assert rob([2, 3, 2]) == 3
    assert rob([1, 2, 3, 1]) == 4
    assert rob([0]) == 0
