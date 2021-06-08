"""
Given an array of integers citations where citations[i] is the number of citations a researcher received
for their ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.

A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers
have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

You must write an algorithm that runs in logarithmic time.

Constraints:
    n == citations.length
    1 <= n <= 105
    0 <= citations[i] <= 1000
    citations is sorted in ascending order.
"""
from typing import List


def h_index(citations: List[int]) -> int:
    n: int = len(citations)
    left: int = 0
    right: int = n - 1

    while left <= right:
        mid: int = (left + right) // 2

        if citations[mid] >= n - mid:
            right = mid - 1
        else:
            left = mid + 1

    return n - left


if __name__ == '__main__':
    assert h_index([0, 1, 3, 5, 6]) == 3
    assert h_index([1, 2, 100]) == 2
