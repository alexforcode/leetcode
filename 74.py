"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
  - Integers in each row are sorted from left to right.
  - The first integer of each row is greater than the last integer of the previous row.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10**4 <= matrix[i][j], target <= 10**4
"""
from typing import List


def search_list(lst: List[int], target: int) -> bool:
    start: int = 0
    end: int = len(lst) - 1

    while start <= end:
        mid: int = start + (end - start) // 2
        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            return True

    return False


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    start: int = 0
    end: int = len(matrix) - 1

    while start <= end:
        mid: int = start + (end - start) // 2
        if matrix[mid][0] > target:
            end = mid - 1
        elif matrix[mid][-1] < target:
            start = mid + 1
        else:
            return search_list(matrix[mid], target)

    return False


if __name__ == '__main__':
    assert search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
