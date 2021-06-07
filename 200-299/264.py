"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Constraints:
    1 <= n <= 1690
"""
from typing import List


def nth_ugly_number(n: int) -> int:
    ugly_nums: List[int] = [1]
    idx_2: int = 0
    idx_3: int = 0
    idx_5: int = 0

    while len(ugly_nums) < n:
        ugly_nums.append(min(2 * ugly_nums[idx_2], 3 * ugly_nums[idx_3], 5 * ugly_nums[idx_5]))

        if ugly_nums[-1] == 2 * ugly_nums[idx_2]:
            idx_2 += 1

        if ugly_nums[-1] == 3 * ugly_nums[idx_3]:
            idx_3 += 1

        if ugly_nums[-1] == 5 * ugly_nums[idx_5]:
            idx_5 += 1

    return ugly_nums[-1]


if __name__ == '__main__':
    assert nth_ugly_number(10) == 12
    assert nth_ugly_number(1) == 1
