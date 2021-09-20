"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Note:
    1 <= S.length <= 20000
    S consists only of English lowercase letters.
"""
from typing import List


def remove_duplicates(s: str) -> str:
    stack: List[str] = [s[0]]

    for char in s[1:]:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


if __name__ == '__main__':
    assert remove_duplicates('abbaca') == 'ca'
    assert remove_duplicates('aaaaaaa') == 'a'
