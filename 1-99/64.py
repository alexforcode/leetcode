"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100
"""
from typing import List, Union


def min_path_sum(grid: List[List[int]]) -> int:
    rows: int = len(grid)
    cols: int = len(grid[0])

    min_path: List[Union[float, int]] = [float('inf') for _ in range(cols+1)]
    min_path[1] = 0

    for row in range(1, rows+1):
        new_min_path: List[Union[float, int]] = [float('inf') for _ in range(cols+1)]

        for col in range(1, cols+1):
            new_min_path[col] = grid[row-1][col-1] + min(min_path[col], new_min_path[col-1])

        min_path = new_min_path

    return min_path[-1]


if __name__ == '__main__':
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12
