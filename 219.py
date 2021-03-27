"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that
nums[i] == nums[j] and abs(i - j) <= k.

Constraints:
    1 <= nums.length <= 10**5
    -10**9 <= nums[i] <= 10**9
    0 <= k <= 10**5
"""
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    # Time: O(n*k)
    # Space: O(n)

    if len(nums) == len(set(nums)):
        return False

    if len(nums) <= k + 1:
        return True

    for i in range(len(nums) - k):
        j: int = i + k + 1
        if len(nums[i:j]) != len(set(nums[i:j])):
            return True

    return False


if __name__ == '__main__':
    assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True
    assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True
    assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert contains_nearby_duplicate([99, 99], 2) is True
    assert contains_nearby_duplicate([1, 2], 2) is False
    assert contains_nearby_duplicate([1, 2, 3, 4, 5, 6, 6], 2) is True
