"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there won't be input like 3a or 2[4].

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""
from typing import List


def decode_string(s: str) -> str:
    nums: List[int] = []
    strings: List[str] = []
    result: str = ''
    idx: int = 0

    while idx < len(s):
        if s[idx].isdigit():
            num: int = 0
            while s[idx].isdigit():
                num = 10 * num + int(s[idx])
                idx += 1
            nums.append(num)
        elif s[idx] == '[':
            strings.append(result)
            result = ''
            idx += 1
        elif s[idx] == ']':
            temp: str = strings.pop()
            num: int = nums.pop()
            for _ in range(num):
                temp += result
            result = temp
            idx += 1
        else:
            result += s[idx]
            idx += 1

    return result


if __name__ == '__main__':
    assert decode_string('3[a]2[bc]') == 'aaabcbc'
    assert decode_string('3[a2[c]]') == 'accaccacc'
    assert decode_string('2[abc]3[cd]ef') == 'abcabccdcdcdef'
    assert decode_string('abc3[cd]xyz') == 'abccdcdcdxyz'
