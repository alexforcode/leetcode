"""
Reverse bits of a given 32 bits unsigned integer.

Note:
    Note that in some languages such as Java, there is no unsigned integer type.
        In this case, both input and output will be given as a signed integer type.
        They should not affect your implementation, as the integer's internal binary representation is the same,
        whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation.
        Therefore, in Example 2 above, the input represents the signed integer -3 and
        the output represents the signed integer -1073741825.

Follow up:
    If this function is called many times, how would you optimize it?

Constraints:
    The input must be a binary string of length 32
"""


def reverse_bits(n: int) -> int:
    bits: str = bin(n)[2:]
    bits = bits[::-1] + ''.join(['0' for _ in range(32 - len(bits))])

    return int(bits, 2)


if __name__ == '__main__':
    assert reverse_bits(0b00000010100101000001111010011100) == 964176192
    assert reverse_bits(0b11111111111111111111111111111101) == 3221225471
