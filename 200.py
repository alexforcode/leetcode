"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""
from typing import List


def search_neighbour(grid: List[List[str]], i: int, j: int) -> None:
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
        return
    grid[i][j] = '0'
    search_neighbour(grid, i+1, j)
    search_neighbour(grid, i-1, j)
    search_neighbour(grid, i, j+1)
    search_neighbour(grid, i, j-1)


def num_islands(grid: List[List[str]]) -> int:
    count: int = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count += 1
                search_neighbour(grid, i, j)

    return count


if __name__ == '__main__':
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]

    assert num_islands(grid) == 3
