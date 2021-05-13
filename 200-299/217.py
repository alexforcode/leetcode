"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Constraints:
    1 <= nums.length <= 10**5
    -10**9 <= nums[i] <= 10**9
"""
from typing import List, Set


def contains_duplicate_1(nums: List[int]) -> bool:
    # Time: O(n*log(n)) + O(n)
    # Space: O(1)

    if len(nums) == 1:
        return False

    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

    return False


def contains_duplicate_2(nums: List[int]) -> bool:
    # Time: O(n)
    # Space: O(n)

    unique: Set[int] = set(nums)

    return len(nums) != len(unique)


if __name__ == '__main__':
    assert contains_duplicate_1([1, 2, 3, 1]) is True
    assert contains_duplicate_1([1, 2, 3, 4]) is False
    assert contains_duplicate_1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate_1([1]) is False

    assert contains_duplicate_2([1, 2, 3, 1]) is True
    assert contains_duplicate_2([1, 2, 3, 4]) is False
    assert contains_duplicate_2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate_2([1]) is False
