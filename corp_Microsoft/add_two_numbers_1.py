class Solution:
    def add_two_numbers(self, l1, l2):
        cur1, cur2 = l1, l2
        cur = dummy = ListNode(-1)
        sum_ = 0

        while cur1 or cur2:
            sum_ = sum_ // 10

            if cur1:
                sum_ += cur1.val
                cur1 = cur1.next

            if cur2:
                sum_ += cur2.val
                cur2 = cur2.next

            cur.next = ListNode(sum_ % 10)
            cur = cur.next

        if sum_ >= 10:
            cur.next = ListNode(1)

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
