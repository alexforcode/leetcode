"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Constraints:
    0 <= intervals.length <= 10**4
    intervals[i].length == 2
    0 <= intervals[i][0] <= intervals[i][1] <= 10**5
    intervals is sorted by intervals[i][0] in ascending order.
    newInterval.length == 2
    0 <= newInterval[0] <= newInterval[1] <= 10**5
"""
from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if not intervals:
        return [new_interval]

    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    result: List[List[int]] = []

    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


if __name__ == '__main__':
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert insert([], [5, 7]) == [[5, 7]]
    assert insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert insert([[1, 5]], [2, 7]) == [[1, 7]]
