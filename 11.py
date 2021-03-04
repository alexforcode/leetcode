"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""
from typing import List


def max_area(height: List[int]) -> int:
    area: int = 0
    left: int = 0
    right: int = len(height) - 1

    while left < right:
        if height[left] < height[right]:
            area = max((area, height[left] * (right - left)))
            left += 1
        else:
            area = max((area, height[right] * (right - left)))
            right -= 1

    return area


if __name__ == '__main__':
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
