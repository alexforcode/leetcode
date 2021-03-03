"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import Dict, List


def two_sums(nums: List[int], target: int) -> List[int]:
    diffs: Dict[int, int] = dict()

    for i, val in enumerate(nums):
        diff: int = target - val

        if diff in diffs.keys():
            return [diffs[diff], i]

        diffs[val] = i


if __name__ == '__main__':
    assert two_sums([2, 7, 11, 15], 9) == [0, 1]
    assert two_sums([3, 2, 4], 6) == [1, 2]
    assert two_sums([3, 3], 6) == [0, 1]
