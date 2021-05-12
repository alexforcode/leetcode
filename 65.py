"""
A valid number can be split up into these components (in order):
    1. A decimal number or an integer.
    2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
    1. (Optional) A sign character (either '+' or '-').
    2. One of the following formats:
      - At least one digit, followed by a dot '.'.
      - At least one digit, followed by a dot '.', followed by at least one digit.
      - A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):
    1. (Optional) A sign character (either '+' or '-').
    2. At least one digit.

For example,
all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
"53.5e93", "-123.456e789"],
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Constraints:
    1 <= s.length <= 20
    s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
from typing import List, Set


DIGITS: Set[str] = {str(num) for num in range(10)}


def is_int(s: List[str], signed: bool) -> bool:
    if len(s) == 0:
        return False

    if s[0] in '-+' and signed:
        s = s[1:]

    if len(s) == 0:
        return False

    for char in s:
        if char not in DIGITS:
            return False

    return True


def is_float(s: List[str]) -> bool:
    try:
        dot_idx: int = s.index('.')
        before: List[str] = s[:dot_idx]
        after: List[str] = s[dot_idx+1:]

        if before and before[0] in '+-':
            before = before[1:]

        if before and not is_int(before, False):
            return False

        if after and not is_int(after, False):
            return False

        return bool(before) or bool(after)

    except Exception:
        return False


def is_sci(s: List[str]) -> bool:
    try:
        e_idx: int = s.index('e')
        before: List[str] = s[:e_idx]
        after: List[str] = s[e_idx+1:]

        if not before or not after:
            return False

        if not is_int(before, True) and not is_float(before):
            return False

        return is_int(after, True)

    except Exception:
        return False


def is_number(s: str) -> bool:
    s: List[str] = [char for char in s.strip().lower()]

    if not s:
        return False

    return is_int(s, True) or is_float(s) or is_sci(s)


if __name__ == '__main__':
    assert is_number('0') is True
    assert is_number('e') is False
    assert is_number('.') is False
    assert is_number('.1') is True

    assert is_number('0089') is True
    assert is_number('+3.14') is True
    assert is_number('2e10') is True
    assert is_number('-123.456e789') is True

    assert is_number('abc') is False
    assert is_number('99e2.5') is False
    assert is_number('-+6') is False
    assert is_number('95a54e53') is False
    assert is_number('4e+') is False
