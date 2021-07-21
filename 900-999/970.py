"""
Given three integers x, y, and bound, return a list of all the powerful integers
that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

Constraints:
    1 <= x, y <= 100
    0 <= bound <= 10**6
"""
from typing import List, Set


def powerful_integers(x: int, y: int, bound: int) -> List[int]:
    result: Set = set()

    def get_power_list(val: int) -> List[int]:
        power_list: List[int] = [1]

        if val != 1:
            while power_list[-1] <= bound:
                power_list.append(power_list[-1] * val)
            power_list.pop()

        return power_list

    x_list: List[int] = get_power_list(x)
    y_list: List[int] = get_power_list(y)

    for x_val in x_list:
        for y_val in y_list:
            if x_val + y_val > bound:
                break
            result.add(x_val + y_val)

    return list(result)


if __name__ == '__main__':
    assert powerful_integers(2, 3, 10) == [2, 3, 4, 5, 7, 9, 10]
    assert powerful_integers(3, 5, 15) == [2, 4, 6, 8, 10, 14]
