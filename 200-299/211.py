"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
        word may contain dots '.' where dots can be matched with any letter.

Constraints:
    1 <= word.length <= 500
    word in addWord consists lower-case English letters.
    word in search consist of '.' or lower-case English letters.
    At most 50000 calls will be made to addWord and search.
"""
from collections import defaultdict
from typing import DefaultDict, List


class WordDictionary:
    def __init__(self) -> None:
        self.words: DefaultDict[int, List[str]] = defaultdict(list)

    def add_word(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        for obj in self.words[len(word)]:
            for idx, char in enumerate(obj):
                if word[idx] != '.' and word[idx] != char:
                    break
            else:
                return True

        return False


if __name__ == '__main__':
    word_dict = WordDictionary()
    word_dict.add_word("bad")
    word_dict.add_word("dad")
    word_dict.add_word("mad")
    print(word_dict.search("pad"))  # False
    print(word_dict.search("bad"))  # True
    print(word_dict.search(".ad"))  # True
    print(word_dict.search("b.."))  # True
