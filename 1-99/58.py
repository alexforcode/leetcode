"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Constraints:
    1 <= s.length <= 10**4
    s consists of only English letters and spaces ' '.
"""


def length_of_last_word(s: str) -> int:
    count: int = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            count += 1
        elif count:
            return count

    return count


if __name__ == '__main__':
    assert length_of_last_word(' ') == 0
    assert length_of_last_word('Hello World') == 5
    assert length_of_last_word('Hello') == 5
    assert length_of_last_word('Hello ') == 5
