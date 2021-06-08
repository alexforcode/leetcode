"""
Given an array of integers citations where citations[i] is the number of citations a researcher received
for their ith paper, return compute the researcher's h-index.

A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers
have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

Constraints:
    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000
"""
from typing import List


def h_index(citations: List[int]) -> int:
    buckets: List[int] = [0] * (len(citations) + 1)

    for citation in citations:
        buckets[min(citation, len(citations))] += 1

    papers: int = 0

    for bucket in range(len(buckets) - 1, -1, -1):
        papers += buckets[bucket]

        if papers >= bucket:
            return bucket


if __name__ == '__main__':
    assert h_index([3, 0, 6, 1, 5]) == 3
    assert h_index([1, 3, 1]) == 1
