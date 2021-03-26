"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t.
If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Constraints:
    1 <= s.length, t.length <= 105
    s and t consist of English letters.
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t or len(t) > len(s):
        return ''

    char_map: Counter = Counter(t)
    unique: int = len(char_map.keys())
    window_char: Counter = Counter()
    matches: int = 0
    result: str = ''
    i: int = 0
    j: int = -1

    while i < len(s):
        if matches < unique:
            if j == len(s) - 1:
                return result

            j += 1
            window_char[s[j]] += 1
            if 0 < char_map[s[j]] == window_char[s[j]]:
                matches += 1
        else:
            window_char[s[i]] -= 1
            if char_map[s[i]] > 0 and window_char[s[i]] == char_map[s[i]] - 1:
                matches -= 1
            i += 1

        if matches == unique:
            if not result:
                result = s[i:j + 1]
            elif (j - i + 1) < len(result):
                result = s[i:j + 1]

    return result


if __name__ == '__main__':
    assert min_window('ADOBECODEBANC', 'ABC') == 'BANC'
    assert min_window('a', 'a') == 'a'
    assert min_window('aa', 'aa') == 'aa'
