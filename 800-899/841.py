"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1,
and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where
N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Note:
    1 <= rooms.length <= 1000
    0 <= rooms[i].length <= 1000
    The number of keys in all rooms combined is at most 3000.
"""
from typing import List


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    seen: List[bool] = [False] * len(rooms)
    seen[0] = True

    keys: List[int] = [*rooms[0]]

    while keys:
        cur_key: int = keys.pop()
        seen[cur_key] = True

        for new_key in rooms[cur_key]:
            if not seen[new_key]:
                keys.append(new_key)

    return all(seen)


if __name__ == '__main__':
    assert can_visit_all_rooms([[1], [2], [3], []]) is True
    assert can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]) is False
