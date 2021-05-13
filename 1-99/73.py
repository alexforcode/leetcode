"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2**31 <= matrix[i][j] <= 2**31 - 1
"""
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    first_col: bool = False

    for row in range(rows):
        if matrix[row][0] == 0:
            first_col = True
        for col in range(1, cols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(1, rows):
        for col in range(1, cols):
            if not matrix[row][0] or not matrix[0][col]:
                matrix[row][col] = 0

    if matrix[0][0] == 0:
        for col in range(cols):
            matrix[0][col] = 0

    if first_col:
        for row in range(rows):
            matrix[row][0] = 0


if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix)
    print(matrix)  # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix)
    print(matrix)  # [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
