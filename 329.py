"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 2**31 - 1
"""
from typing import List, Optional, Tuple


def longest_increasing_path(matrix: List[List[int]]) -> int:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    cache: List[List[Optional[int]]] = [[None] * cols for _ in range(rows)]
    steps: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_valid_point(i: int, j: int) -> bool:
        return rows > i >= 0 and cols > j >= 0

    def longest_inc_path_from_point(i: int, j: int) -> int:
        if not cache[i][j]:

            max_path_from_point: int = 0
            for step in steps:
                step_i: int = i + step[0]
                step_j: int = j + step[1]

                if is_valid_point(step_i, step_j) and matrix[i][j] < matrix[step_i][step_j]:
                    max_path_from_point = max(max_path_from_point, longest_inc_path_from_point(step_i, step_j))

            cache[i][j] = max_path_from_point + 1

        return cache[i][j]

    max_path: int = 0
    for i in range(rows):
        for j in range(cols):
            max_path = max(max_path, longest_inc_path_from_point(i, j))

    return max_path


if __name__ == '__main__':
    assert longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert longest_increasing_path([[1]]) == 1
