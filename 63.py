"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
"""
from typing import List


def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    if obstacle_grid[0] == 1 or obstacle_grid[-1][-1] == 1:
        return 0

    rows: int = len(obstacle_grid)
    cols: int = len(obstacle_grid[0])

    paths: List[int] = [0 for _ in range(cols+1)]
    paths[1] = 1

    for row in range(1, rows+1):
        new_paths: List[int] = [0]

        for col in range(1, cols+1):
            if obstacle_grid[row-1][col-1] == 1:
                new_paths.append(0)
            else:
                new_paths.append(new_paths[-1] + paths[col])

        paths = new_paths

    return paths[-1]


if __name__ == '__main__':
    assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths_with_obstacles([[0, 1], [0, 0]]) == 1
