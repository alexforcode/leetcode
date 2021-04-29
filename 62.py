"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Constraints:
    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10**9.
"""
from typing import List


def unique_paths(m: int, n: int) -> int:
    paths: List[int] = [1 for _ in range(n)]

    for row in range(m-1):
        new_paths: List[int] = [1]

        for col in range(1, n):
            new_paths.append(new_paths[-1] + paths[col])

        paths = new_paths

    return paths[-1]


if __name__ == '__main__':
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(7, 3) == 28
    assert unique_paths(3, 3) == 6
