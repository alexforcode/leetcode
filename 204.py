"""
Count the number of prime numbers less than a non-negative number, n.

Constraints:
    0 <= n <= 5 * 10**6
"""
import math
from typing import List


def count_primes(n: int) -> int:
    if n <= 2:
        return 0

    sieve: List[bool] = [True] * n
    sieve[0] = sieve[1] = False

    for idx in range(4, n, 2):
        sieve[idx] = False

    idx: int = 3
    while idx <= int(math.sqrt(n)):
        if sieve[idx]:
            for j in range(idx * 2, n, idx):
                sieve[j] = False
        idx += 2

    count: int = 0
    for prime in sieve:
        if prime:
            count += 1

    return count


if __name__ == '__main__':
    assert count_primes(10) == 4
    assert count_primes(0) == 0
    assert count_primes(1) == 0

