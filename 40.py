"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""
from typing import List


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []
    candidates.sort()

    def dfs(cur: List[int], index: int, remain: int) -> None:
        if remain < 0:
            return

        if remain == 0:
            result.append(list(cur))
            return

        for i in range(index, len(candidates)):
            if i == index or candidates[i] != candidates[i-1]:
                cur.append(candidates[i])
                dfs(cur, i + 1, remain - candidates[i])
                cur.pop()

    dfs([], 0, target)

    return result


if __name__ == '__main__':
    assert combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert combination_sum_2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
