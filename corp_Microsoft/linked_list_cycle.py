class Solution:
    def has_cycle(self, head):
        if head is None:
            return False

        slow = fast = head

        while True:
            if fast.next is None or fast.next.next is None:
                break

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
