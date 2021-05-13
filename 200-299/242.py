"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Constraints:
    1 <= s.length, t.length <= 5 * 10**4
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t) or sorted(s) != sorted(t):
        return False

    return True


def is_anagram_using_counter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_map: Counter[str, int] = Counter(s)

    for char in t:
        if char in char_map.keys():
            char_map[char] -= 1
        else:
            return False

    for val in char_map.values():
        if val != 0:
            return False

    return True


if __name__ == '__main__':
    assert is_anagram('anagram', 'nagaram') is True
    assert is_anagram('aacc', 'ccac') is False
    assert is_anagram('rat', 'car') is False

    assert is_anagram_using_counter('anagram', 'nagaram') is True
    assert is_anagram_using_counter('aacc', 'ccac') is False
    assert is_anagram_using_counter('rat', 'car') is False
