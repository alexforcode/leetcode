"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
"""
from typing import List


def get_str_from_list(line: List[str], max_width: int, line_width: int) -> str:
        num_places: int = len(line) - 1
        missing_spaces: int = max_width - line_width
        spaces: str = ''
        rem_count: int = 0

        if num_places:
            spaces = ' ' * (missing_spaces // num_places)
            rem_count = missing_spaces % num_places

        string: str = ''
        for idx, val in enumerate(line):
            string += val
            if idx < rem_count:
                string += spaces + ' ' * 2
            elif idx != len(line) - 1:
                string += spaces + ' '

        string += ' ' * (max_width - len(string))

        return string


def get_str_from_last_line(line: List[str], max_width: int) -> str:
    string: str = ''

    for word in line:
        string += word + ' '

    string = string[:-1] + ' ' * (max_width - len(string) + 1)

    return string


def full_justify(words: List[str], max_width: int) -> List[str]:
    result: List[str] = []
    line: List[str] = []
    line_width: int = 0

    for word in words:
        new_width: int = len(word) if not line_width else line_width + 1 + len(word)

        if new_width <= max_width:
            line.append(word)
            line_width = new_width
        else:
            result.append(get_str_from_list(line, max_width, line_width))
            line.clear()
            line.append(word)
            line_width = len(word)

    result.append(get_str_from_last_line(line, max_width))

    return result


if __name__ == '__main__':
    assert full_justify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    assert full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    assert full_justify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
                         "computer.", "Art", "is", "everything", "else", "we", "do"], 20) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
    assert full_justify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6) == [
        "Listen",
        "to    ",
        "many, ",
        "speak ",
        "to   a",
        "few.  "]