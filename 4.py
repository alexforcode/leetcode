"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

Follow up: The overall run time complexity should be O(log(m+n)).
"""
from typing import List


def find_median(nums1: List[int], nums2: List[int]) -> float:
    first: List[int]
    second: List[int]
    first, second = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    len_f: int = len(first)
    len_s: int = len(second)
    merg_len: int = len_f + len_s

    med_idx = (merg_len + 1) // 2

    low: int = 0
    high: int = min(len_f, med_idx)
    while low < high:
        n: int = (low + high) // 2
        m: int = med_idx - n
        if m > 0 and second[m-1] > first[n]:
            low = n + 1
        else:
            high = n

    n: int = low
    m: int = med_idx - n

    cur = first[n-1] if m == 0 or n > 0 and first[n-1] >= second[m-1] else second[m-1]

    if merg_len % 2:
        return cur

    nxt = first[n] if m == len_s or n < len_f and first[n] <= second[m] else second[m]

    return (cur + nxt) / 2


if __name__ == '__main__':
    assert find_median([1, 3], [2]) == 2.0
    assert find_median([1, 2], [3, 4]) == 2.5
    assert find_median([0, 1, 2, 3, 4], [0, 2, 6, 7]) == 2.0
    assert find_median([0, 0], [0, 0]) == 0.0
    assert find_median([], [1]) == 1.0
    assert find_median([2], []) == 2.0
