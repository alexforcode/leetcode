"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    if k == 0:
        return [[]]

    if n < k:
        return []

    without_last: List[List[int]] = combine(n-1, k)

    with_last: List[List[int]] = [[n] + combo for combo in combine(n-1, k-1)]

    return without_last + with_last


if __name__ == '__main__':
    print(combine(4, 2))
    # [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]

    print(combine(1, 1))
    # [[1]]
