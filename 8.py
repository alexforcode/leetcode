"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'.
       Read this character in if it is either. This determines if the final result is negative or positive respectively.
       Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit character or the end of the input is reached.
       The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
       If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1],
       then clamp the integer so that it remains in the range.
       Specifically, integers less than -2**31 should be clamped to -2**31,
       and integers greater than 2**31 - 1 should be clamped to 2**31 - 1.
    6. Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""
from typing import Set


def my_atoi(s: str) -> int:
    if not s:
        return 0

    res: int = 0
    index: int = 0
    neg_flag: int = 1
    digits: Set[str] = set('0123456789')
    pos_lim: int = 2**31 - 1
    neg_lim: int = -2**31

    while index < len(s) and s[index] == ' ':
        index += 1

    if index < len(s) and s[index] == '-':
        index += 1
        neg_flag = -1
    elif index < len(s) and s[index] == '+':
        index += 1

    while index < len(s) and s[index] in digits:
        res = res * 10 + int(s[index])
        index += 1

    res *= neg_flag

    if res < neg_lim:
        return max(res, neg_lim)
    return min(res, pos_lim)


if __name__ == '__main__':
    assert my_atoi('') == 0
    assert my_atoi('42') == 42
    assert my_atoi('   -42') == -42
    assert my_atoi('+-12') == 0
    assert my_atoi('4193 with words') == 4193
    assert my_atoi('words and 987') == 0
    assert my_atoi('-91283472332') == -2147483648
