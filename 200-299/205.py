"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Constraints:
    1 <= s.length <= 5 * 10**4
    t.length == s.length
    s and t consist of any valid ascii character.
"""
from typing import Dict, Set


def is_isomorphic(s: str, t: str) -> bool:
    char_map: Dict[str, str] = dict()
    t_mapped: Set[str] = set()

    for s_char, t_char in zip(s, t):
        if s_char in char_map:
            if char_map[s_char] != t_char:
                return False
        elif t_char in t_mapped:
            return False
        else:
            char_map[s_char] = t_char
            t_mapped.add(t_char)

    return True


if __name__ == '__main__':
    assert is_isomorphic('egg', 'add') is True
    assert is_isomorphic('foo', 'bar') is False
    assert is_isomorphic('paper', 'title') is True
    assert is_isomorphic('badc', 'baba') is False
