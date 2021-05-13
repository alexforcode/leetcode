"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Constraints:
    0 <= x <= 2**31 - 1
"""
from typing import Union


def my_sqrt(x: int) -> int:
    start: int = 0
    end: int = x

    while start <= end:
        mid: int = start + (end - start) // 2
        if mid * mid > x:
            end = mid - 1
        elif mid * mid < x:
            start = mid + 1
        else:
            return mid

    return end


def my_sqrt_imp(x: int) -> int:
    # https://en.wikipedia.org/wiki/Newton%27s_method
    result: Union[float, int] = x

    while not result * result - x < 1:
        result = (result + x / result) / 2

    return int(result)


if __name__ == '__main__':
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2

    assert my_sqrt_imp(4) == 2
    assert my_sqrt_imp(8) == 2
