"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
from typing import Dict, Tuple


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    def helper(i: int, j: int, memo: Dict[Tuple[int, int], bool]) -> bool:
        if i >= len(s1) or j >= len(s2):
            return s1[i:] + s2[j:] == s3[i+j:]

        if (i, j) in memo:
            return memo[(i, j)]

        result: bool = False

        if s1[i] == s3[i+j] and helper(i+1, j, memo):
            result = True
        elif s2[j] == s3[i+j] and helper(i, j+1, memo):
            result = True

        memo[(i, j)] = result

        return result

    return helper(0, 0, {})


if __name__ == '__main__':
    assert is_interleave('aabcc', 'dbbca', 'aadbbcbcac') is True
    assert is_interleave('aabcc', 'dbbca', 'aadbbbaccc') is False
    assert is_interleave('', '', '') is True
