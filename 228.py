"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b

Constraints:
    0 <= nums.length <= 20
    -2**31 <= nums[i] <= 2**31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.
"""
from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    if not nums:
        return []

    if len(nums) == 1:
        return [str(nums[0])]

    result: List[str] = []
    start: int = 0
    cur: int = 0

    while cur < len(nums)-1:
        if nums[cur] + 1 != nums[cur+1]:
            result.append(f'{nums[start]}->{nums[cur]}' if start != cur else f'{nums[start]}')
            start = cur + 1
        cur += 1

    result.append(f'{nums[start]}->{nums[cur]}' if start != cur else f'{nums[start]}')

    return result


if __name__ == '__main__':
    assert summary_ranges([0, 1, 2, 4, 5, 7]) == ['0->2', '4->5', '7']
    assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ['0', '2->4', '6', '8->9']
    assert summary_ranges([0, 2, 3, 4, 6, 8, 9, 10, 11]) == ['0', '2->4', '6', '8->11']
    assert summary_ranges([]) == []
    assert summary_ranges([-1]) == ['-1']
    assert summary_ranges([0]) == ['0']
