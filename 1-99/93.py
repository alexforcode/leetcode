"""
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s.
You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and
cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245",
"192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Constraints:
    0 <= s.length <= 3000
    s consists of digits only.
"""
from typing import List


def restore_ip_addresses(s: str) -> List[str]:
    parts: int = 4

    if 3 * parts < len(s) < parts:
        return []

    results: List[List[str]] = [[]]

    while parts > 0:
        new_results: List[List[str]] = []

        for result in results:
            used_chars: int = sum((len(part) for part in result))
            remain: int = len(s) - used_chars

            if 3 * (parts - 1) >= remain - 3 >= parts - 1 and 100 <= int(s[used_chars:used_chars+3]) <= 255:
                new_results.append(result + [s[used_chars:used_chars+3]])

            if 3 * (parts - 1) >= remain - 2 >= parts - 1 and 10 <= int(s[used_chars:used_chars+2]):
                new_results.append(result + [s[used_chars:used_chars+2]])

            if 3 * (parts - 1) >= remain - 1 >= parts - 1:
                new_results.append(result + [s[used_chars]])

        parts -= 1
        results = new_results

    return ['.'.join(result) for result in results]


if __name__ == '__main__':
    print(restore_ip_addresses('25525511135'))
    # ['255.255.11.135', '255.255.111.35']

    print(restore_ip_addresses('0000'))
    # ['0.0.0.0']

    print(restore_ip_addresses('1111'))
    # ['1.1.1.1']

    print(restore_ip_addresses('010010'))
    # ['0.10.0.10', '0.100.1.0']

    print(restore_ip_addresses('101023'))
    # ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']
