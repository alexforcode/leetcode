"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice
and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place
with O(1) extra memory.

Constraints:
    1 <= nums.length <= 3 * 10**4
    -10**4 <= nums[i] <= 10**4
    nums is sorted in ascending order.
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    count: int = 2

    for index in range(2, len(nums)):
        if nums[index] != nums[count-2]:
            nums[count] = nums[index]
            count += 1

    return count


if __name__ == '__main__':
    assert remove_duplicates([1, 1, 1, 2, 2, 3]) == 5
    assert remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
