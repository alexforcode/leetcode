"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
"""
from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    max_side: int = 0
    square_sides: List[int] = [0] * cols

    for row in range(rows):
        new_square_sides: List[int] = [int(matrix[row][0])] + [0 for _ in range(cols - 1)]

        for col in range(1, cols):
            if matrix[row][col] == '1':
                new_square_sides[col] = 1 + min(new_square_sides[col - 1], square_sides[col], square_sides[col - 1])

        max_side = max(max_side, max(new_square_sides))
        square_sides = new_square_sides

    return max_side ** 2


if __name__ == '__main__':
    matrix: List[List[str]] = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0'],
    ]
    assert maximal_square(matrix) == 4

    matrix = [
        ['0', '1'],
        ['1', '0'],
    ]
    assert maximal_square(matrix) == 1

    assert maximal_square([['0']]) == 0
