"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Constraints:
    0 <= rowIndex <= 33
"""
from typing import List


def get_row(row_index: int) -> List[int]:
    cur_row: List[int] = []
    prev_row: List[int] = []

    for index in range(row_index+1):
        cur_row = [1 for _ in range(index+1)]

        for i in range(1, len(cur_row)-1):
            cur_row[i] = prev_row[i-1] + prev_row[i]

        prev_row = cur_row

    return cur_row


if __name__ == '__main__':
    assert get_row(3) == [1, 3, 3, 1]
    assert get_row(0) == [1]
    assert get_row(1) == [1, 1]
    assert get_row(4) == [1, 4, 6, 4, 1]
