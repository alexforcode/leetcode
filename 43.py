"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
from typing import List


def multiply(num1: str, num2: str) -> str:
    tmp_lst: List[int] = [0] * (len(num1) + len(num2))

    for i in range(len(num1)-1, -1, -1):
        carry: int = 0
        for j in range(len(num2)-1, -1, -1):
            tmp: int = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + carry
            carry = (tmp_lst[i+j+1] + tmp) // 10
            tmp_lst[i+j+1] = (tmp_lst[i+j+1] + tmp) % 10
        tmp_lst[i] += carry

    result = ''.join(map(str, tmp_lst))

    return result.lstrip('0') or '0'


if __name__ == '__main__':
    assert multiply('2', '3') == '6'
    assert multiply('123', '456') == '56088'
    assert multiply('0', '456') == '0'
