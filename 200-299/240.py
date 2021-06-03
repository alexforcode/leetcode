"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix.
The matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -10**9 <= matix[i][j] <= 10**9
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -10**9 <= target <= 10**9
"""
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    row: int = 0
    col: int = cols - 1

    while row < rows and col >= 0:
        if target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
        else:
            return True

    return False


if __name__ == '__main__':
    matrix: List[List[int]] = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    assert search_matrix(matrix, 5) is True
    assert search_matrix(matrix, 20) is False
