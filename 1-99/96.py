"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of
unique values from 1 to n.

Constraints:
    1 <= n <= 19
"""
from typing import List


def num_trees(n: int) -> int:
    memo: List[int] = [-1] * (n + 1)

    def helper(vals: int) -> int:
        if vals <= 1:
            return 1

        if memo[vals] != -1:
            return memo[vals]

        count: int = 0

        for val in range(1, vals + 1):
            count += helper(val - 1) * helper(vals - val)

        memo[vals] = count

        return count

    return helper(n)


if __name__ == '__main__':
    assert num_trees(3) == 5
    assert num_trees(1) == 1
