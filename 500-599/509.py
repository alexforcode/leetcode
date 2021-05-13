"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Constraints:
    0 <= n <= 30
"""
from typing import List


def fib_list(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    nums: List[int] = [0] * (n+1)
    nums[1] = 1

    for idx in range(2, len(nums)):
        nums[idx] = nums[idx-1] + nums[idx-2]

    return nums[-1]


def fib_rec(n: int) -> int:
    if n <= 1:
        return n

    return fib_rec(n-1) + fib_rec(n-2)


def fib_pointers(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    prev1: int = 0
    prev2: int = 1
    cur: int = 0

    for _ in range(2, n+1):
        cur = prev1 + prev2
        prev1 = prev2
        prev2 = cur

    return cur


if __name__ == '__main__':
    assert fib_list(2) == 1
    assert fib_list(3) == 2
    assert fib_list(4) == 3
    assert fib_list(0) == 0

    assert fib_rec(2) == 1
    assert fib_rec(3) == 2
    assert fib_rec(4) == 3
    assert fib_rec(0) == 0

    assert fib_pointers(2) == 1
    assert fib_pointers(3) == 2
    assert fib_pointers(4) == 3
    assert fib_pointers(0) == 0
