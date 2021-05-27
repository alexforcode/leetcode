"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
        which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Constraints:
    1 <= n <= 2**31 - 1
"""
from typing import Set


def is_happy(n: int) -> bool:
    seen: Set[int] = set()

    while n > 1 and n not in seen:
        seen.add(n)
        n = sum([int(char) * int(char) for char in str(n)])

    return n == 1


if __name__ == '__main__':
    assert is_happy(19) is True
    assert is_happy(239) is True
    assert is_happy(2) is False
    assert is_happy(240) is False
