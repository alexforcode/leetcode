"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of
some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Constraints:
    1 <= n <= 10**4
"""
from typing import List


def num_squares(n: int) -> int:
    memo: List[int] = [0, 1]

    while len(memo) <= n:
        memo.append(1 + min(memo[-i * i] for i in range(1, int(len(memo) ** 0.5) + 1)))

    return memo[n]


if __name__ == '__main__':
    assert num_squares(12) == 3
    assert num_squares(13) == 2
