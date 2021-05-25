"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

Constraints:
    0 <= n <= 10**4
"""


def trailing_zeroes(n: int) -> int:
    zeroes: int = 0
    pow_of_5: int = 5

    while pow_of_5 <= n:
        zeroes += n // pow_of_5
        pow_of_5 *= 5

    return zeroes


if __name__ == '__main__':
    assert trailing_zeroes(3) == 0
    assert trailing_zeroes(5) == 1
    assert trailing_zeroes(0) == 0
