"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
    1 <= nums.length <= 10**4
    -2**31 <= nums[i] <= 2**31 - 1

Follow up: Could you minimize the total number of operations done?
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    if len(nums) == 1:
        return

    start: int = 0
    index: int = 0

    while index < len(nums):
        if nums[start] != 0:
            start += 1
        else:
            if nums[index] != 0:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1

        index += 1


if __name__ == '__main__':
    lst = [0, 1, 0, 3, 12]
    move_zeroes(lst)
    print(lst)

    lst = [1, 3, 4, 2, 6, 7]
    move_zeroes(lst)
    print(lst)

    lst = [0]
    move_zeroes(lst)
    print(lst)

    lst = [5, 7, 9, 5, 0, 0]
    move_zeroes(lst)
    print(lst)
