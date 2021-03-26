"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater
than or equal to target.
If there is no such subarray, return 0 instead.

Constraints:
    1 <= target <= 10**9
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**5
"""
from typing import List, Union


def min_subarray_len(target: int, nums: List[int]) -> int:
    result: Union[float, int] = float('inf')
    left: int = 0
    cur_sum: int = 0

    for i in range(len(nums)):
        cur_sum += nums[i]

        while cur_sum >= target:
            result = min(result, i + 1 - left)
            cur_sum -= nums[left]
            left += 1

    return result if result != float('inf') else 0


if __name__ == '__main__':
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
