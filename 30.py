"""
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once,
in any order, and without any intervening characters.

You can return the answer in any order.

Constraints:
    1 <= s.length <= 10**4
    s consists of lower-case English letters.
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    words[i] consists of lower-case English letters.
"""
from collections import Counter
from typing import List, Dict


def find_substring(s: str, words: List[str]) -> List[int]:
    result: List[int] = []
    word_len: int = len(words[0])
    perm_len: int = word_len * len(words)

    if len(s) < perm_len:
        return result

    word_count: Counter = Counter(words)

    for i in range(len(s) - perm_len + 1):
        unused: Dict = dict(word_count)

        for j in range(i, i + perm_len, word_len):
            check: str = s[j:j+word_len]
            occur: int = unused.get(check, -1)

            if occur <= 0:
                break

            unused[check] = occur - 1
            if not occur - 1:
                del unused[check]

        if not unused:
            result.append(i)

    return result


if __name__ == '__main__':
    found = find_substring('barfoothefoobarman', ['foo', 'bar'])
    print(found)  # [0, 9]

    found = find_substring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word'])
    print(found)  # []

    found = find_substring('barfoofoobarthefoobarman', ['bar', 'foo', 'the'])
    print(found)  # [6, 9, 12]

    found = find_substring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good'])
    print(found)  # [8]
