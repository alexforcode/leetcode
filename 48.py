"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Constraints:
    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    if len(matrix) == 1:
        return

    # transpose the matrix
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # flip the matrix horizontally
    for row in range(len(matrix)):
        left: int = 0
        right: int = len(matrix) - 1

        while left < right:
            matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
            left += 1
            right -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    print(matrix)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    print(matrix)  # [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    matrix = [[1]]
    rotate(matrix)
    print(matrix)  # [[1]]

    matrix = [[1, 2], [3, 4]]
    rotate(matrix)
    print(matrix)  # [[3, 1], [4, 2]]
