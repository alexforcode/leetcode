"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and
you may return the result in any order.

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot
        load all elements into the memory at once?
"""
from typing import Dict, List


def intersect1(nums1: List[int], nums2: List[int]) -> List[int]:
    result: List[int] = []
    p1: int = 0
    p2: int = 0

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1

    return result


def intersect2(nums1: List[int], nums2: List[int]) -> List[int]:
    result: List[int] = []
    val_map: Dict[int, int] = {}

    for val in nums1:
        if val not in val_map:
            val_map[val] = 1
        else:
            val_map[val] += 1

    for val in nums2:
        if val in val_map and val_map[val] > 0:
            result.append(val)
            val_map[val] -= 1

    return result


if __name__ == '__main__':
    lst1, lst2 = [1, 2, 2, 1], [2, 2]
    print(intersect1(lst1, lst2))  # [2, 2]

    lst1, lst2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(intersect1(lst1, lst2))  # [4, 9]

    lst1, lst2 = [1, 2, 2, 1], [2, 2]
    print(intersect2(lst1, lst2))  # [2, 2]

    lst1, lst2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(intersect2(lst1, lst2))  # [4, 9]
