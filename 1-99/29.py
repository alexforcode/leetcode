"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−2**31, 2**31 − 1].
For this problem, assume that your function returns 2**31 − 1 when the division result overflows.

Constraints:
    -2**31 <= dividend, divisor <= 2**31 - 1
    divisor != 0
"""


def divide(dividend: int, divisor: int) -> int:
    pos_lim: int = 2**31 - 1
    neg_lim: int = -2**31
    sign: int = -1 if (dividend < 0) != (divisor < 0) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient: int = 0
    while dividend >= divisor:
        count: int = 1
        accum: int = divisor
        while dividend >= accum + accum:
            accum += accum
            count += count
        dividend -= accum
        quotient += count

    quotient *= sign

    return neg_lim if quotient < neg_lim else min(quotient, pos_lim)


if __name__ == '__main__':
    assert divide(10, 3) == 3
    assert divide(7, -3) == -2
    assert divide(-1, -1) == 1
    assert divide(0, 1) == 0
    assert divide(1, 1) == 1
