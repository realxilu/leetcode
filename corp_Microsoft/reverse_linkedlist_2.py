class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        # do it for m - 1 times
        for i in range(m - 1):
            pre = pre.next

        start = pre.next
        then = start.next
        # draw a diagram to quickly understand the following
        for i in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        return dummy.next

# m, n are the left and right position instead of values of its element

# 1) why use dummy
# it's always more convinent to introduce dummy
# 2) why stop at m - 1
# 3) why n - m

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
