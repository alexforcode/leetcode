"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    result: str = ''

    if not strs:
        return result

    min_len: int = len(min(strs, key=len))

    for i in range(min_len):
        char = strs[0][i]

        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return result

        result += char

    return result


if __name__ == '__main__':
    assert longest_common_prefix(["flower", "flow", "flight"]) == 'fl'
    assert longest_common_prefix(["dog", "racecar", "car"]) == ''
    assert longest_common_prefix(["", "racecar", "car"]) == ''
    assert longest_common_prefix([""]) == ''
    assert longest_common_prefix([]) == ''
