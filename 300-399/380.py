"""
Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
        false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
        false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least
        one element exists when this method is called). Each element must have the same probability of being returned.

Constraints:
    -2**31 <= val <= 2**31 - 1
    At most 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.

Follow up: Could you implement the functions of the class with each function works in average O(1) time?
"""
from typing import Dict
from random import choice


class RandomizedSet:
    _obj: Dict

    def __init__(self):
        self._obj = dict()

    def insert(self, val: int) -> bool:
        if self._obj.get(val, None) == val:
            return False
        else:
            self._obj[val] = val
            return True

    def remove(self, val: int) -> bool:
        if self._obj.get(val, None) == val:
            del self._obj[val]
            return True
        else:
            return False

    def get_random(self) -> int:
        if not self._obj:
            return False
        else:
            return choice(list(self._obj.keys()))


if __name__ == '__main__':
    rand_set: RandomizedSet = RandomizedSet()
    print(rand_set.get_random())  # False
    print(rand_set.insert(1))     # True
    print(rand_set.remove(2))     # False
    print(rand_set.insert(2))     # True
    print(rand_set.get_random())  # 1 or 2
    print(rand_set.remove(1))     # True
    print(rand_set.insert(2))     # False
    print(rand_set.get_random())  # 2
