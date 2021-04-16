"""
You are given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

Constraints:
    0 <= s.length <= 300
    s consists of lower-case and upper-case English letters, digits or
        one of the following characters "!@#$%^&*()_+-=',.:".
    The only space character in s is ' '.
"""


def count_segments(s: str) -> int:
    count: int = 0
    for idx in range(len(s)):
        if (idx == 0 or s[idx-1] == ' ') and s[idx] != ' ':
            count += 1

    return count


if __name__ == '__main__':
    assert count_segments('Hello, my name is John') == 5
    assert count_segments('Hello') == 1
    assert count_segments('love live! mu\'sic forever') == 4
    assert count_segments('') == 0
    assert count_segments(' ') == 0
    assert count_segments('      ') == 0
