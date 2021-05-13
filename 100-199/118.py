"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Constraints:
    1 <= numRows <= 30
"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    triangle: List[List[int]] = []

    for row_num in range(num_rows):
        row: List[int] = [1 for _ in range(row_num+1)]

        for i in range(1, len(row)-1):
            row[i] = triangle[row_num-1][i-1] + triangle[row_num-1][i]

        triangle.append(row)

    return triangle


if __name__ == '__main__':
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate(1) == [[1]]
