"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Note:
    s.length will be between 1 and 50,000.
    s will only consist of "0" or "1" characters.
"""


def count_binary_substrings(s: str) -> int:
    result: int = 0
    prev_count: int = 0
    idx: int = 0

    while idx < len(s):
        cur_count: int = 1

        while idx < len(s) - 1 and s[idx] == s[idx+1]:
            cur_count += 1
            idx += 1

        if prev_count > 0:
            result += min(prev_count, cur_count)

        prev_count = cur_count
        idx += 1

    return result


if __name__ == '__main__':
    assert count_binary_substrings('00110011') == 6
    assert count_binary_substrings('10101') == 4
