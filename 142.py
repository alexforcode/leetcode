"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node that
tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    slow: ListNode = head
    fast: ListNode = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow

    return None
