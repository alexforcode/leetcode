"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Constraints:
    1 <= s.length <= 3 * 10*5
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    Every number and running calculation will fit in a signed 32-bit integer.
"""
from typing import List, Set, Tuple, Union


def calculate(s: str) -> int:
    digits: Set[str] = {str(num) for num in range(10)}
    expression: List[Union[int, str]] = ['(']

    for char in s:
        if char == ' ':
            continue
        if char not in digits:
            expression.append(char)
        elif isinstance(expression[-1], int):
            expression[-1] = expression[-1] * 10 + int(char)
        else:
            expression.append(int(char))

    expression.append(')')

    def evaluate(idx: int) -> Tuple[int, int]:
        calc: int = 0
        operator: str = '+'

        while expression[idx] != ')':
            atom: Union[str, int] = expression[idx]

            if atom == '+' or atom == '-':
                operator = atom
            else:
                if isinstance(atom, int):
                    num: int = atom
                else:
                    num, idx = evaluate(idx + 1)

                if operator == '+':
                    calc += num
                else:
                    calc -= num

            idx += 1

        return calc, idx

    result, _ = evaluate(1)

    return result


if __name__ == '__main__':
    assert calculate('1 + 1') == 2
    assert calculate(' 2-1 + 2 ') == 3
    assert calculate('(1+(4+5+2)-3)+(6+8)') == 23
    assert calculate('+48 + -48') == 0
