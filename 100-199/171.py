"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].
"""


def title_to_number(col_title: str) -> int:
    idx: int = 0

    for char in col_title:
        idx = idx * 26 + ord(char) - ord('A') + 1

    return idx


if __name__ == '__main__':
    assert title_to_number('A') == 1
    assert title_to_number('AB') == 28
    assert title_to_number('ZY') == 701
    assert title_to_number('FXSHRXW') == 2147483647
