"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image
(from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill,
and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels
with the newColor.

At the end, return the modified image.

Note:
    The length of image and image[0] will be in the range [1, 50].
    The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    if image[sr][sc] == new_color:
        return image

    def fill(row: int, col: int, color: int) -> None:
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[row]) or image[row][col] != color:
            return
        image[row][col] = new_color

        fill(row-1, col, color)
        fill(row+1, col, color)
        fill(row, col-1, color)
        fill(row, col+1, color)

    fill(sr, sc, image[sr][sc])

    return image


if __name__ == '__main__':
    assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
