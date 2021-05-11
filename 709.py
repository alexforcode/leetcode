"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


def to_lower_case(string: str) -> str:
    if not string:
        return string

    result: str = ''

    for char in string:
        result += chr(ord(char) + 32) if ord(char) in range(65, 91) else char

    return result


if __name__ == '__main__':
    assert to_lower_case('Hello') == 'hello'
    assert to_lower_case('hello') == 'hello'
    assert to_lower_case('LOVELY') == 'lovely'
