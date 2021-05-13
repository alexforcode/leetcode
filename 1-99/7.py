"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

Constraints:
    -2**31 <= x <= 2**31 - 1
"""


def reverse(x: int) -> int:
    if x == 0:
        return 0

    neg_limit = -0x80000000  # hex(-2**31)
    pos_limit = 0x7fffffff   # hex(2**31-1)

    if x > 0:
        rev_int = int(str(x)[::-1])
        return rev_int if rev_int & pos_limit == rev_int else 0
    else:
        rev_int = -int(str(abs(x))[::-1])
        return rev_int if rev_int & neg_limit == neg_limit else 0


if __name__ == '__main__':
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(0) == 0
