"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode()
    current = result

    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        val = val1 + val2 + carry
        carry = val // 10
        current.next = ListNode(val % 10)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(add_two_numbers(l1, l2))

    l1 = ListNode(0)
    l2 = ListNode(0)
    print(add_two_numbers(l1, l2))

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
    l2 = ListNode(9, ListNode(9, ListNode(9)))
    print(add_two_numbers(l1, l2))
