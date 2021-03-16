"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough space
to hold additional elements from nums2.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10**9 <= nums1[i], nums2[i] <= 10**9
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if n == 0:
        return
    if not nums1:
        nums1.extend(nums2)
        return

    point1: int = m - 1
    point2: int = n - 1
    index: int = len(nums1) - 1

    while point2 >= 0:
        if point1 >= 0 and nums1[point1] > nums2[point2]:
            nums1[index] = nums1[point1]
            point1 -= 1
        else:
            nums1[index] = nums2[point2]
            point2 -= 1
        index -= 1


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    m, n = 3, 3
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, nums2 = [1, 2], []
    m, n = 2, 0
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, nums2 = [], [2, 5, 6]
    m, n = 0, 3
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, nums2 = [2, 0], [1]
    m, n = 1, 1
    merge(nums1, m, nums2, n)
    print(nums1)
