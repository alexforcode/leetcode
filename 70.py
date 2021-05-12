"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
    1 <= n <= 45
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    cur: int = 2
    prev: int = 1

    for _ in range(3, n+1):
        cur, prev = cur + prev, cur

    return cur


if __name__ == '__main__':
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
