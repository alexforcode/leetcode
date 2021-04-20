"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]

    sums: List[int] = [0] * (len(triangle) + 1)

    for row in triangle[::-1]:
        for idx, num in enumerate(row):
            sums[idx] = num + min(sums[idx], sums[idx+1])

    return sums[0]


if __name__ == '__main__':
    assert minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert minimum_total([[-1], [2, 3], [1, -1, -3]]) == -1
    assert minimum_total([[-10]]) == -10
