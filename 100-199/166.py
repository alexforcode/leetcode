"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 10**4 for all the given inputs.

Constraints:
    -2*31 <= numerator, denominator <= 2*31 - 1
    denominator != 0
"""
from typing import List, Dict


def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return '0'

    decimal: List[str] = []

    if (numerator < 0 < denominator) or (denominator < 0 < numerator):
        decimal.append('-')

    dividend: int = abs(numerator)
    divisor: int = abs(denominator)
    remainder: int = dividend % divisor
    decimal.append(str(dividend // divisor))

    if not remainder:
        return ''.join(decimal)

    decimal.append('..')

    rem_positions: Dict = dict()
    while remainder != 0:
        if remainder in rem_positions.keys():
            decimal.insert(rem_positions[remainder], '(')
            decimal.append(')')
            break

        rem_positions[remainder] = len(decimal)
        remainder *= 10
        decimal.append(str(remainder // divisor))
        remainder %= divisor

    return ''.join(decimal)


if __name__ == '__main__':
    assert fraction_to_decimal(1, 2) == '0.5'
    assert fraction_to_decimal(2, 1) == '2'
    assert fraction_to_decimal(2, 3) == '0.(6)'
    assert fraction_to_decimal(4, 333) == '0.(012)'
    assert fraction_to_decimal(1, 5) == '0.2'
