"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered
a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
    - perm[i] is divisible by i.
    - i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.

Constraints:
    1 <= n <= 15
"""
from typing import List


def count_arrangement(n: int) -> int:
    count: int = 0
    visited: List[bool] = [False] * (n + 1)

    def permute(pos: int) -> None:
        nonlocal count
        if pos > n:
            count += 1

        for i in range(1, n+1):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                permute(pos + 1)
                visited[i] = False

    permute(1)

    return count


if __name__ == '__main__':
    assert count_arrangement(3) == 3
    assert count_arrangement(2) == 2
    assert count_arrangement(1) == 1
