class Solution:
    # recursive
    def reverse_list(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverse_list(head.next)
        head.next.next = head
        head.next = None

        return new_head

    # iterative, in-place
    def reverse_list_iter(self, head):
        prev, cur = None, head

        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_

        return prev


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
