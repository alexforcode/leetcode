"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if
the given words are sorted lexicographicaly in this alien language.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
"""
from typing import List, Dict


def compare(word1: str, word2: str, char_map: Dict[str, int]) -> bool:
    p1: int = 0
    p2: int = 0

    while p1 < len(word1) and p2 < len(word2):
        if char_map[word1[p1]] > char_map[word2[p2]]:
            return False
        elif char_map[word1[p1]] < char_map[word2[p2]]:
            return True
        p1 += 1
        p2 += 1

    if len(word1) > len(word2):
        return False

    return True


def is_alien_sorted(words: List[str], order: str) -> bool:
    if len(words) <= 1:
        return True

    char_map: Dict[str, int] = {}

    for idx, char in enumerate(order):
        char_map[char] = idx

    for idx in range(len(words)-1):
        if not compare(words[idx], words[idx+1], char_map):
            return False

    return True


if __name__ == '__main__':
    assert is_alien_sorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz') is True
    assert is_alien_sorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz') is False
    assert is_alien_sorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz') is False
