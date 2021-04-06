"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.

Constraints:
    1 <= bad <= n <= 2**31 - 1
"""


class VersionControl:
    _bad: int

    def __init__(self, bad_version: int):
        self._bad = bad_version

    def is_bad_version(self, check_version: int):
        return self._bad <= check_version


def first_bad_version(n: int, vers: VersionControl) -> int:
    start: int = 1
    end: int = n

    while start < end:
        mid = start + (end - start) // 2
        if vers.is_bad_version(mid):
            end = mid
        else:
            start = mid + 1

    return start


if __name__ == '__main__':
    vc = VersionControl(4)
    assert first_bad_version(5, vc) == 4

    vc = VersionControl(1)
    assert first_bad_version(1, vc) == 1

    vc = VersionControl(10)
    assert first_bad_version(50, vc) == 10
