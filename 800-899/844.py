"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""
from itertools import zip_longest
from typing import Generator


def get_valid_chars(s: str) -> Generator[str, None, None]:
    skip: int = 0

    for char in reversed(s):
        if char == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield char


def backspace_compare(s: str, t: str) -> bool:
    return all(c_s == c_t for c_s, c_t in zip_longest(get_valid_chars(s), get_valid_chars(t)))


if __name__ == '__main__':
    assert backspace_compare('ab#c', 'ad#c') is True
    assert backspace_compare('ab##', 'c#d#') is True
    assert backspace_compare('a##c', '#a#c') is True
    assert backspace_compare('a#c', 'b') is False
