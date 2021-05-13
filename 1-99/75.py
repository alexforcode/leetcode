"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is 0, 1, or 2.
"""
from typing import List


def sort_colors(nums: List[int]) -> None:
    if len(nums) == 1:
        return

    start: int = 0
    end: int = len(nums) - 1
    current: int = 0

    while current <= end and start < end:
        if nums[current] == 0:
            nums[start], nums[current] = nums[current], nums[start]
            start += 1
            current += 1
        elif nums[current] == 2:
            nums[end], nums[current] = nums[current], nums[end]
            end -= 1
        else:
            current += 1


if __name__ == '__main__':
    colors = [2, 0, 2, 1, 1, 1]
    sort_colors(colors)
    print(colors)

    colors = [2, 0, 1]
    sort_colors(colors)
    print(colors)

    colors = [1, 2, 0]
    sort_colors(colors)
    print(colors)

    colors = [1]
    sort_colors(colors)
    print(colors)

    colors = [0]
    sort_colors(colors)
    print(colors)
