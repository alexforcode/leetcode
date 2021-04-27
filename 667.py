"""
 Given two integers n and k, you need to construct a list which contains n different positive integers ranging
 from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|]
has exactly k distinct integers.

If there are multiple answers, print any of them.

Note:
    The n and k are in the range 1 <= k < n <= 10**4.
"""
from typing import List


def construct_array(n: int, k: int) -> List[int]:
    result: List[int] = list(range(1, n - k))

    for i in range(k + 1):
        if i % 2 == 0:
            result.append(n - k + i // 2)
        else:
            result.append(n - i // 2)

    return result


if __name__ == '__main__':
    assert construct_array(3, 1) == [1, 2, 3]
    assert construct_array(3, 2) == [1, 3, 2]
    assert construct_array(6, 3) == [1, 2, 3, 6, 4, 5]
