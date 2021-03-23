"""
Given two binary strings a and b, return their sum as a binary string.

Constraints:
    1 <= a.length, b.length <= 10**4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""


def add_binary(a: str, b: str) -> str:
    max_len: int = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry: int = 0
    result: str = ''

    for i in reversed(range(max_len)):
        carry += 1 if a[i] == '1' else 0
        carry += 1 if b[i] == '1' else 0
        result = ('1' if carry % 2 == 1 else '0') + result
        carry = 0 if carry < 2 else 1

    if carry != 0:
        result = '1' + result

    return result


if __name__ == '__main__':
    assert add_binary('11', '1') == '100'
    assert add_binary('1010', '1011') == '10101'
