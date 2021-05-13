"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Constraints:
    1 <= n <= 20
"""
from typing import List


def generate_matrix(n: int) -> List[List[int]]:
    if n == 1:
        return [[1]]

    matrix: List[List[int]] = [[0] * n for _ in range(n)]

    row_start: int = 0
    row_end: int = n-1
    col_start: int = 0
    col_end: int = n-1

    count: int = 1

    while row_start <= row_end and col_start <= col_end:

        for i in range(col_start, col_end+1):
            matrix[row_start][i] = count
            count += 1
        row_start += 1

        for i in range(row_start, row_end+1):
            matrix[i][col_end] = count
            count += 1
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):
                matrix[row_end][i] = count
                count += 1
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start-1, -1):
                matrix[i][col_start] = count
                count += 1
            col_start += 1

    return matrix


if __name__ == '__main__':
    assert generate_matrix(1) == [[1]]
    assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
