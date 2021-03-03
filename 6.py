"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""
from typing import List


def zigzag_convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    direction: int = -1
    row: int = 0
    zigzag: List[List[str]] = [[] for _ in range(num_rows)]

    for char in s:
        zigzag[row].append(char)

        if row == 0 or row == num_rows - 1:
            direction *= -1

        row += direction

    for i in range(len(zigzag)):
        zigzag[i] = ''.join(zigzag[i])

    return ''.join(zigzag)


def zigzag_convert_improve(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    step: int = 2 * num_rows - 2
    res: List[str] = []

    for i in range(num_rows):
        for j in range(i, len(s), step):
            res.append(s[j])
            k = j + step - 2 * i
            if i != 0 and i != num_rows - 1 and k < len(s):
                res.append(s[k])

    return ''.join(res)


if __name__ == '__main__':
    assert zigzag_convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert zigzag_convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert zigzag_convert('A', 1) == 'A'
    assert zigzag_convert('AB', 1) == 'AB'

    assert zigzag_convert_improve('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert zigzag_convert_improve('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert zigzag_convert_improve('A', 1) == 'A'
    assert zigzag_convert_improve('AB', 1) == 'AB'
