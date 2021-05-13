"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference,
which means a modification to the input array will be known to the caller as well.

Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    if not nums:
        return 0

    index: int = 0

    while index < len(nums):
        if nums[index] == val:
            del nums[index]
        else:
            index += 1

    return len(nums)


if __name__ == '__main__':
    assert remove_element([3, 2, 2, 3], 3) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
