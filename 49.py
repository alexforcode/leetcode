"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
    1 <= strs.length <= 10**4
    0 <= strs[i].length <= 100
    strs[i] consists of lower-case English letters.
"""
from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    count: defaultdict = defaultdict(list)

    for string in strs:
        count[tuple(sorted(string))].append(string)

    return [val for val in count.values()]


if __name__ == '__main__':
    lst = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    lst = group_anagrams(lst)
    print(lst)  # [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]

    lst = ['']
    lst = group_anagrams(lst)
    print(lst)  # [['']]

    lst = ['a']
    lst = group_anagrams(lst)
    print(lst)  # [['a']]
