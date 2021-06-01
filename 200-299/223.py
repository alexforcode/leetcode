"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Constraints:
    -10**4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10**4
"""


def compute_area(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    x_left_edge: int = max(ax1, bx1)
    x_right_edge: int = min(ax2, bx2)
    x_overlap: int = max(x_right_edge - x_left_edge, 0)

    y_left_edge: int = max(ay1, by1)
    y_right_edge: int = min(ay2, by2)
    y_overlap: int = max(y_right_edge - y_left_edge, 0)

    rect1: int = (ax2 - ax1) * (ay2 - ay1)
    rect2: int = (bx2 - bx1) * (by2 - by1)

    return rect1 + rect2 - y_overlap * x_overlap


if __name__ == '__main__':
    assert compute_area(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2) == 45
    assert compute_area(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2) == 16
