"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate
that is different: for example, if x1 != x1'.

Constraints:
    1 <= matrix.length <= 100
    1 <= matrix[0].length <= 100
    -1000 <= matrix[i] <= 1000
    -10**8 <= target <= 10**8
"""
from collections import Counter
from typing import List


def num_submatrix_sum_target(matrix: List[List[int]], target: int) -> int:
    row_len: int = len(matrix[0])

    for row in matrix:
        row.insert(0, 0)
        for i in range(1, row_len + 1):
            row[i] += row[i - 1]

    result: int = 0
    for i in range(1, row_len + 1):
        for j in range(0, i):
            cur: int = 0
            counter: Counter = Counter([0])
            for row in matrix:
                cur += row[i] - row[j]
                result += counter[cur - target]
                counter[cur] += 1

    return result


if __name__ == '__main__':
    assert num_submatrix_sum_target([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0) == 4
    assert num_submatrix_sum_target([[1, -1], [-1, 1]], 0) == 5
    assert num_submatrix_sum_target([[904]], 0) == 0
