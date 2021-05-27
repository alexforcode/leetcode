"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Constraints:
    0 <= num <= 2**31 - 1

Follow up:
    Could you do it without any loop/recursion in O(1) runtime?
"""


def add_digits(num: int) -> int:
    while num > 9:
        num = sum([int(char) for char in str(num)])

    return num


def add_digits_2(num: int) -> int:
    if num == 0:
        return num

    if num % 9 == 0:
        return 9

    return num % 9


if __name__ == '__main__':
    assert add_digits(38) == 2
    assert add_digits(0) == 0

    assert add_digits_2(38) == 2
    assert add_digits_2(0) == 0
