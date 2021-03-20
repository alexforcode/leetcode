"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,4,4,5,6,7] might become:

    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    nums is sorted and rotated between 1 and n times.
"""
from typing import List


def find_min(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    start: int = 0
    end: int = len(nums) - 1

    while start < end:
        mid: int = start + (end - start) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[start]:
            end = mid
        else:
            end -= 1

    return nums[start]


if __name__ == '__main__':
    assert find_min([1, 3, 5]) == 1
    assert find_min([2, 2, 2, 0, 1]) == 0
    assert find_min([3, 3, 3, 3, 1, 3]) == 1
