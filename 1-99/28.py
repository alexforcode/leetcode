"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Constraints:
    0 <= haystack.length, needle.length <= 5 * 104
    haystack and needle consist of only lower-case English characters.
"""


def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    if not haystack or len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:len(needle)+i] == needle:
            return i

    return -1


if __name__ == '__main__':
    assert str_str('hello', 'll') == 2
    assert str_str('aaaa', 'baa') == -1
    assert str_str('hello', 'hello') == 0
    assert str_str('', '') == 0
    assert str_str('', 'a') == -1
