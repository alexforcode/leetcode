"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3**x.

Constraints:
    -2**31 <= n <= 2**31 - 1

Follow up: Could you solve it without loops/recursion?
"""
import math


def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False

    max_int: int = 2**31 - 1
    max_power: int = int(math.log(max_int, 3))

    return 3**max_power % n == 0


if __name__ == '__main__':
    assert is_power_of_three(27) is True
    assert is_power_of_three(0) is False
    assert is_power_of_three(9) is True
    assert is_power_of_three(45) is False
    assert is_power_of_three(-3) is False
