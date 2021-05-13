"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if len(matrix) == 1:
        return matrix[0]

    result: List[int] = []
    row_start: int = 0
    row_end: int = len(matrix) - 1
    col_start: int = 0
    col_end: int = len(matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:

        for i in range(col_start, col_end+1):
            result.append(matrix[row_start][i])
        row_start += 1

        for i in range(row_start, row_end+1):
            result.append(matrix[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start-1, -1):
                result.append(matrix[i][col_start])
            col_start += 1

    return result


if __name__ == '__main__':
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
