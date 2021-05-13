"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up,
and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Constraints:
    1 <= matchsticks.length <= 15
    0 <= matchsticks[i] <= 109
"""
from typing import List


def make_square(matchsticks: List[int]) -> bool:

    def dfs(idx):
        if idx == len(matchsticks):
            return True

        for side in range(4):
            if sides[side] + matchsticks[idx] > target or sides[side] in sides[side+1:]:
                continue

            sides[side] += matchsticks[idx]

            if dfs(idx+1):
                return True

            sides[side] -= matchsticks[idx]

        return False

    perimeter: int = sum(matchsticks)

    if not perimeter or perimeter % 4 != 0:
        return False

    target: int = perimeter // 4
    matchsticks.sort(reverse=True)

    if matchsticks[0] > target:
        return False

    sides: List[int] = [0] * 4
    idx: int = 0

    while idx < 4 and matchsticks[idx] == target:
        sides[idx] = target
        idx += 1

    return dfs(idx)


if __name__ == '__main__':
    assert make_square([1, 1, 2, 2, 2]) is True
    assert make_square([3, 3, 3, 3, 4]) is False
