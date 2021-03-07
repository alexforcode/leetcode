"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and
returns the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array
will be known to the caller as well.

Constraints:
    0 <= nums.length <= 3 * 10**4
    -10**4 <= nums[i] <= 10**4
    nums is sorted in ascending order.
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    index: int = 0

    while index < len(nums) - 1:
        if nums[index] == nums[index+1]:
            del nums[index]
        else:
            index += 1

    return len(nums)


if __name__ == '__main__':
    assert remove_duplicates([1, 1, 2]) == 2
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
