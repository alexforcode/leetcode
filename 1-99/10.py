"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Constraints:
    0 <= s.length <= 20
    0 <= p.length <= 30
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
from typing import List


def is_match(s: str, p: str) -> bool:
    matched: List[List[bool]] = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    matched[0][0] = True

    for i in range(len(s)+1):
        for j in range(1, len(p)+1):
            pattern: str = p[j-1]

            if pattern == '.':
                matched[i][j] = i != 0 and matched[i-1][j-1]
            elif pattern == '*':
                star: str = p[j-2]
                matched[i][j] = matched[i][j-2] or (i > 0 and matched[i-1][j] and (star == s[i-1] or star == '.'))
            else:
                matched[i][j] = i != 0 and matched[i-1][j-1] and s[i-1] == pattern

    return matched[-1][-1]


if __name__ == '__main__':
    assert is_match('aa', 'a') is False
    assert is_match('aa', 'a*') is True
    assert is_match('ab', '.*') is True
    assert is_match('aab', 'c*a*b') is True
    assert is_match('mississippi', 'mis*is*p*.') is False
