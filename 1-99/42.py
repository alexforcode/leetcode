"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Constraints:
    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105
"""
from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0

    h_len: int = len(height)
    highest_right: List[int] = [0] * h_len
    highest_left: List[int] = [0] * h_len
    depth: int = 0

    for idx in range(h_len-2, -1, -1):
        highest_right[idx] = max(highest_right[idx+1], height[idx+1])

    for idx in range(1, h_len):
        highest_left[idx] = max(highest_left[idx-1], height[idx-1])
        depth += max(0, min(highest_left[idx], highest_right[idx]) - height[idx])

    return depth


if __name__ == '__main__':
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
