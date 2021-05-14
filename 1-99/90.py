"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""
from collections import Counter
from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    num_count: Counter[int, int] = Counter(nums)
    results: List[List[int]] = [[]]

    for num in num_count:
        results += [part + [num]*i for i in range(1, num_count[num]+1) for part in results]

    return results


if __name__ == '__main__':
    print(subsets_with_dup([1, 2, 2]))
    # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    print(subsets_with_dup([0]))
    # [[0]]
