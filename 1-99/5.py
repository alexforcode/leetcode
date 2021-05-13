"""
Given a string s, return the longest palindromic substring in s.

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case)
"""


def longest_palindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    result: str = ''

    for i in range(len(s)):
        palindrome_even = get_palindrome(s, i, i + 1)
        palindrome_odd = get_palindrome(s, i, i)

        if len(palindrome_even) > len(result):
            result = palindrome_even

        if len(palindrome_odd) > len(result):
            result = palindrome_odd

    return result


def get_palindrome(s: str, left: int, right: int) -> str:

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left+1:right]


if __name__ == '__main__':
    assert longest_palindrome('babad') == 'bab'
    assert longest_palindrome('cbbd') == 'bb'
    assert longest_palindrome('ccc') == 'ccc'
    assert longest_palindrome('a') == 'a'
    assert longest_palindrome('ac') == 'a'
    assert longest_palindrome('') == ''
