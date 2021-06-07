"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Constraints:
    -2**31 <= n <= 2**31 - 1
"""


def is_ugly(n: int) -> bool:
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    while n % 3 == 0:
        n //= 3

    while n % 5 == 0:
        n //= 5

    return n == 1


if __name__ == '__main__':
    assert is_ugly(6) is True
    assert is_ugly(8) is True
    assert is_ugly(14) is False
    assert is_ugly(1) is True
