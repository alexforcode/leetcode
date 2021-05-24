"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Constraints:
    1 <= columnNumber <= 2**31 - 1
"""
from collections import deque
from typing import Deque


def convert_to_title(col_num: int) -> str:
    col_idxs: Deque[int] = deque()

    while col_num > 0:
        col_num, idx = divmod(col_num - 1, 26)
        col_idxs.appendleft(idx)

    return ''.join([chr(i + ord('A')) for i in col_idxs])


if __name__ == '__main__':
    assert convert_to_title(1) == 'A'
    assert convert_to_title(28) == 'AB'
    assert convert_to_title(701) == 'ZY'
    assert convert_to_title(2147483647) == 'FXSHRXW'
