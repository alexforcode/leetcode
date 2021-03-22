"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Constraints:
    1 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

Follow up:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""
from typing import List


def rotate1(nums: List[int], k: int) -> None:
    if len(nums) == 1:
        return

    # Brute Force
    # Time: O(len(nums)*k) ~ O(n**2)
    # Space: O(1)

    k %= len(nums)

    for _ in range(k):
        prev: int = nums[-1]
        for i in range(len(nums)):
            nums[i], prev = prev, nums[i]


def rotate2(nums: List[int], k: int) -> None:
    if len(nums) == 1:
        return

    # Using Extra Array
    # Time: O(n)
    # Space: O(n)

    res: List[nums] = [None] * len(nums)

    for i in range(len(nums)):
        res[(i + k) % len(nums)] = nums[i]

    nums[:] = res


def rotate3(nums: List[int], k: int) -> None:
    if len(nums) == 1:
        return

    # Cyclic Replacements
    # Time: O(n)
    # Space: O(1)

    k %= len(nums)
    start_idx: int = 0
    count: int = 0

    while count < len(nums):
        cur_idx: int = start_idx
        cur_val: int = nums[start_idx]
        while True:
            next_idx = (cur_idx + k) % len(nums)
            nums[next_idx], cur_val = cur_val, nums[next_idx]
            cur_idx = next_idx
            count += 1

            if start_idx == cur_idx:
                break
        start_idx += 1


def rotate4(nums: List[int], k: int) -> None:
    if len(nums) == 1:
        return

    # Reverse
    # Time: O(n + (n-k) + k) -> O(2n) -> O(n)
    # Space: O(1)

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    length: int = len(nums)
    k %= length

    reverse(0, length-1)
    reverse(0, k-1)
    reverse(k, length-1)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7]
    rotate1(lst, 3)
    print(lst)  # [5, 6, 7, 1, 2, 3, 4]

    lst = [-1, -100, 3, 99]
    rotate1(lst, 2)
    print(lst)  # [3, 99, -1, -100]

    lst = [1, 2, 3, 4, 5, 6, 7]
    rotate2(lst, 3)
    print(lst)  # [5, 6, 7, 1, 2, 3, 4]

    lst = [-1, -100, 3, 99]
    rotate2(lst, 2)
    print(lst)  # [3, 99, -1, -100]

    lst = [1, 2, 3, 4, 5, 6, 7]
    rotate3(lst, 3)
    print(lst)  # [5, 6, 7, 1, 2, 3, 4]

    lst = [-1, -100, 3, 99]
    rotate3(lst, 2)
    print(lst)  # [3, 99, -1, -100]

    lst = [1, 2, 3, 4, 5, 6, 7]
    rotate4(lst, 3)
    print(lst)  # [5, 6, 7, 1, 2, 3, 4]

    lst = [-1, -100, 3, 99]
    rotate4(lst, 2)
    print(lst)  # [3, 99, -1, -100]
