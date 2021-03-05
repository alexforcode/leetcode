"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

'2': 'abc'
'3': 'def'
'4': 'ghi'
'5': 'jkl'
'6': 'mno'
'7': 'pqrs'
'8': 'tuv'
'9': 'wxyz'

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""
from typing import List, Optional


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []

    result: List[str] = ['']
    char_map: List[Optional[str]] = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for i in range(len(digits)):
        index: int = int(digits[i])
        while len(result[0]) == i:
            permutation: str = result.pop(0)
            for char in char_map[index]:
                result.append(permutation + char)

    return result


if __name__ == '__main__':
    assert letter_combinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert letter_combinations('') == []
    assert letter_combinations('2') == ['a', 'b', 'c']
