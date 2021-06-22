class Solution:
    # recursive
    # the key to any recursive approach is to assume that the solution
    # had _already_ been created
    def reverse_list(self, head):
        if not head or not head.next:
            return head

        # according to the contract, the rec func is supposed to return a new head
        new_head = self.reverse_list(head.next)
        head.next.next = head
        head.next = None

        return new_head

    # iterative, in-place
    def reverse_list_iter(self, head):
        prev, cur = None, head

        while cur:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next

        return prev


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
