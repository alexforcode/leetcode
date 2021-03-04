"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Constraints:
    -2**31 <= x <= 2**31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev_int: int = 0
    while x > rev_int:
        rev_int = rev_int * 10 + x % 10
        x //= 10

    return x == rev_int or x == rev_int // 10


if __name__ == '__main__':
    assert is_palindrome(1) is True
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
    assert is_palindrome(0) is True
    assert is_palindrome(-101) is False
