"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol  Value
I        1
V        5
X        10
L        50
C        100
D        500
M        1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
from typing import Dict


def roman_to_int(s: str) -> int:
    romans: Dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result: int = 0
    index: int = 0

    while index < len(s) - 1:
        if romans[s[index]] >= romans[s[index+1]]:
            result += romans[s[index]]
        else:
            result += romans[s[index+1]] - romans[s[index]]
            index += 1

        index += 1

    if index == len(s) - 1:
        result += romans[s[index]]

    return result


if __name__ == '__main__':
    assert roman_to_int('III') == 3
    assert roman_to_int('IV') == 4
    assert roman_to_int('IX') == 9
    assert roman_to_int('LVIII') == 58
    assert roman_to_int('MCMXCIV') == 1994
