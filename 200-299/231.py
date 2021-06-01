"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2**x.

Constraints:
    -231 <= n <= 231 - 1
"""


def is_power_of_two(n: int) -> bool:
    return n > 0 and not n & (n - 1)


if __name__ == '__main__':
    assert is_power_of_two(1) is True
    assert is_power_of_two(16) is True
    assert is_power_of_two(3) is False
    assert is_power_of_two(4) is True
    assert is_power_of_two(5) is False
