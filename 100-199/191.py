"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
    Note that in some languages, such as Java, there is no unsigned integer type.
        In this case, the input will be given as a signed integer type.
        It should not affect your implementation, as the integer's internal binary representation is the same,
        whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation.
        Therefore, in Example 3, the input represents the signed integer. -3.

Constraints:
    The input must be a binary string of length 32.

Follow up:
    If this function is called many times, how would you optimize it?
"""


def hamming_weight(n: int) -> int:
    return sum(char == '1' for char in bin(n)[2:])


if __name__ == '__main__':
    assert hamming_weight(0b00000000000000000000000000001011) == 3
    assert hamming_weight(0b00000000000000000000000010000000) == 1
    assert hamming_weight(0b11111111111111111111111111111101) == 31
