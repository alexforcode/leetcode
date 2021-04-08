"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List, Set


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1: Set[int] = set(nums1)
    set2: Set[int] = set(nums2)

    if len(set1) < len(set2):
        return [x for x in set1 if x in set2]
    else:
        return [x for x in set2 if x in set1]


if __name__ == '__main__':
    lst1, lst2 = [1, 2, 2, 1], [2, 2]
    print(intersection(lst1, lst2))  # [2]

    lst1, lst2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(intersection(lst1, lst2))  # [9,4]
