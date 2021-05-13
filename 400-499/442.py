"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""
from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    output: List[int] = []

    for i in range(len(nums)):
        index: int = abs(nums[i]) - 1
        if nums[index] < 0:
            output.append(index + 1)
        nums[index] = -nums[index]

    return output


if __name__ == '__main__':
    assert find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
