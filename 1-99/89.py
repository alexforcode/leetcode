"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

Constraints:
    1 <= n <= 16
"""
from typing import List


def gray_code(n: int) -> List[int]:
    gray: List[int] = [0]

    for num in range(n):
        gray += [x + 2**num for x in reversed(gray)]

    return gray


if __name__ == '__main__':
    print(gray_code(2))
    # [0,1,3,2]

    print(gray_code(1))
    # [0,1]
