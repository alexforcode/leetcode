"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Constraints:
    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List, Set


def eval_rpn(tokens: List[str]) -> int:
    operators: Set[str] = {'+', '-', '*', '/'}
    stack: List[int] = []

    for token in tokens:
        if token in operators:
            right: int = stack.pop()
            left: int = stack.pop()

            if token == '/':
                stack.append(int(left / float(right)))
            else:
                stack.append(eval(str(left) + token + str(right)))
        else:
            stack.append(int(token))

    return stack[-1]


if __name__ == '__main__':
    assert eval_rpn(['2', '1', '+', '3', '*']) == 9
    assert eval_rpn(['4', '13', '5', '/', '+']) == 6
    assert eval_rpn(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22
