"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    all_subs: List[List[int]] = []
    bits: int = 2 ** len(nums)

    for bit in range(bits):
        sub: List[int] = []

        for num in nums:
            if bit % 2 == 1:
                sub.append(num)
            bit //= 2

        all_subs.append(sub)

    return all_subs


if __name__ == '__main__':
    assert subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert subsets([0]) == [[], [0]]
