"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    left: int = 0
    right: int = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == '__main__':
    string = ['h', 'e', 'l', 'l', 'o']
    reverse_string(string)
    print(string)

    string = ['H', 'a', 'n', 'n', 'a', 'h']
    reverse_string(string)
    print(string)

