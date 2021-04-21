"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Constraints:
    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of digits '0' and '1'.
    1 <= m, n <= 100
"""
from typing import List


def find_max_form(strs: List[str], m: int, n: int) -> int:
    matrix: List[List[int]] = [[0] * (n+1) for _ in range(m+1)]

    for s in strs:
        zeros: int = s.count('0')
        ones: int = s.count('1')
        for i in range(m, zeros-1, -1):
            for j in range(n, ones-1, -1):
                matrix[i][j] = max(matrix[i][j], matrix[i-zeros][j-ones] + 1)

    return matrix[m][n]


if __name__ == '__main__':
    assert find_max_form(['10', '0001', '111001', '1', '0'], 5, 3) == 4
    assert find_max_form(['10', '0', '1'], 1, 1) == 2
