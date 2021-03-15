"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less
than 150 combinations for the given input.

Constraints:
    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    All elements of candidates are distinct.
    1 <= target <= 500
"""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []

    def dfs(cur: List[int], cur_sum: int, index: int) -> None:
        if cur_sum > target:
            return

        if cur_sum == target:
            result.append(cur)
            return

        for i in range(index, len(candidates)):
            dfs(cur + [candidates[i]], cur_sum + candidates[i], i)

    dfs([], 0, 0)

    return result


if __name__ == '__main__':
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combination_sum([2], 1) == []
    assert combination_sum([1], 1) == [[1]]
    assert combination_sum([1], 2) == [[1,1]]
