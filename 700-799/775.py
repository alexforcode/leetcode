"""
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Note:
    A will be a permutation of [0, 1, ..., A.length - 1].
    A will have length in range [1, 5000].
    The time limit for this problem has been reduced.
"""
from typing import List


def is_ideal_permutation(lst: List[int]) -> bool:
    max_val: int = lst[0]

    for idx in range(len(lst) - 2):
        max_val = max(max_val, lst[idx])
        if max_val > lst[idx + 2]:
            return False

    return True


if __name__ == '__main__':
    assert is_ideal_permutation([1, 0, 2]) is True
    assert is_ideal_permutation([1, 2, 0]) is False
