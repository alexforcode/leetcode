"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Constraints
    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

Follow up: Could you solve it in-place with O(1) extra space?
"""


def reverse_words(s: str) -> str:
    return ' '.join([word for word in s.strip().split() if word][::-1])


if __name__ == '__main__':
    assert reverse_words('the sky is blue') == 'blue is sky the'
    assert reverse_words('  hello world  ') == 'world hello'
    assert reverse_words('a good   example') == 'example good a'
    assert reverse_words('  Bob    Loves  Alice   ') == 'Alice Loves Bob'
    assert reverse_words('Alice does not even like bob') == 'bob like even not does Alice'
