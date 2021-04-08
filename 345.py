"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
from typing import List, Set


def reverse_vowels(s: str) -> str:
    if len(s) < 2:
        return s

    result: List[str] = list(s)
    vowels: Set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    left: int = 0
    right: int = len(result) - 1

    while left < right:
        if result[left] in vowels and result[right] in vowels:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        else:
            if result[left] not in vowels:
                left += 1
            if result[right] not in vowels:
                right -= 1

    return ''.join(result)


if __name__ == '__main__':
    assert reverse_vowels('hello') == 'holle'
    assert reverse_vowels('leetcode') == 'leotcede'
