"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    count_and_say(1) = "1"
    count_and_say(n) is the way you would "say" the digit string from count_and_say(n-1),
      which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups
so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Given a positive integer n, return the nth term of the count-and-say sequence.

Constraints:
    1 <= n <= 30
"""


def count_and_say(n: int) -> str:
    if n == 1:
        return '1'

    prev: str = count_and_say(n-1)
    result: str = ''
    char_count: int = 0

    pointer: str = prev[0]

    for char in prev:
        if pointer == char:
            char_count += 1
        else:
            result += str(char_count) + pointer
            pointer = char
            char_count = 1

    result += str(char_count) + pointer

    return result


if __name__ == '__main__':
    assert count_and_say(1) == '1'
    assert count_and_say(4) == '1211'
    assert count_and_say(5) == '111221'
    assert count_and_say(6) == '312211'
    assert count_and_say(7) == '13112221'
    assert count_and_say(8) == '1113213211'
    assert count_and_say(9) == '31131211131221'
