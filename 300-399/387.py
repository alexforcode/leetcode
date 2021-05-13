"""
Given a string, find the first non-repeating character in it and return its index.
If it doesn't exist, return -1.

Note: You may assume the string contains only lowercase English letters.
"""
from collections import Counter


def first_uniq_char(s: str) -> int:
    counter: Counter = Counter(s)

    for idx, val in enumerate(s):
        if counter[val] == 1:
            return idx

    return -1


if __name__ == '__main__':
    assert first_uniq_char('leetcode') == 0
    assert first_uniq_char('loveleetcode') == 2
