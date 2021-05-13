"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


def is_alphanumeric(char: str) -> bool:
    return 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90 or 48 <= ord(char) <= 57


def is_palindrome(s: str) -> bool:
    start: int = 0
    end: int = len(s) - 1

    while start < end:
        if not is_alphanumeric(s[start]):
            start += 1
            continue
        if not is_alphanumeric(s[end]):
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1

    return True


if __name__ == '__main__':
    assert is_palindrome('A man, a plan, a canal: Panama') is True
    assert is_palindrome('race a car') is False
