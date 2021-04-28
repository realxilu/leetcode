class Solution:
    def addTwoNumbers(self, l1, l2):
        cur1, cur2 = l1, l2
        # [innovative][sentry] the use of sentry will make the while clean and easy to read
        cur = dummy = ListNode(-1)
        _sum = 0

        while cur1 or cur2:
            # example 14 // 10 = 1 (carry)
            # example 0  // 10 = 0
            _sum = _sum // 10

            if cur1:
                _sum += cur1.val
                cur1 = cur1.next

            if cur2:
                _sum += cur2.val
                cur2 = cur2.next

            # example 14 % 10 = 4
            cur.next = ListNode(_sum % 10)
            cur = cur.next

        # don't forget about the last digit
        if _sum >= 10:
            cur.next = ListNode(1)

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
