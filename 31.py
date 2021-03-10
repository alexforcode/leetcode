"""
Implement next permutation, which rearranges numbers into
the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order
(i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""
from typing import List


def next_permutation(nums: List[int]) -> None:
    if len(nums) == 1:
        return

    index: int = len(nums) - 2

    while index >= 0 and nums[index] >= nums[index+1]:
        index -= 1

    if index >= 0:
        pointer: int = len(nums) - 1
        while pointer >= index and nums[pointer] <= nums[index]:
            pointer -= 1
        nums[index], nums[pointer] = nums[pointer], nums[index]

    nums[index+1:] = nums[index+1:][::-1]


if __name__ == '__main__':
    lst = [1, 2, 3]
    next_permutation(lst)
    assert lst == [1, 3, 2]

    lst = [3, 2, 1]
    next_permutation(lst)
    assert lst == [1, 2, 3]

    lst = [3, 2, 1]
    next_permutation(lst)
    assert lst == [1, 2, 3]

    lst = [6, 2, 1, 5, 4, 3, 0]
    next_permutation(lst)
    assert lst == [6, 2, 3, 0, 1, 4, 5]

    lst = [1]
    next_permutation(lst)
    assert lst == [1]
