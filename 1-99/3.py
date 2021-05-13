"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""
from typing import Set


def longest_substring_length(s: str) -> int:
    if not s:
        return 0

    i: int = 0
    j: int = 0
    max_length: int = 0
    unique: Set[str] = set()

    while j < len(s):
        if s[j] in unique:
            unique.discard(s[i])
            i += 1
        else:
            unique.add(s[j])
            j += 1
            max_length = max(len(unique), max_length)

    return max_length


if __name__ == '__main__':
    assert longest_substring_length('abcabcbb') == 3
    assert longest_substring_length('bbbbb') == 1
    assert longest_substring_length('pwwkew') == 3
    assert longest_substring_length('') == 0
    assert longest_substring_length('abcadabc')
