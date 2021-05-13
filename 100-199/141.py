"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
    The number of the nodes in the list is in the range [0, 10**4].
    -10**5 <= Node.val <= 10**5
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    if not head.next:
        return False

    slow: ListNode = head
    fast: ListNode = head

    while slow != fast:
        if not fast or not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return True
