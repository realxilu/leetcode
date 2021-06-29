class Solution:
    def addTwoNumbers(self, l1, l2):
        cur1, cur2 = l1, l2
        # sentinel node
        cur = dummy = ListNode(-1)
        _sum = 0

        while cur1 or cur2:
            # example 14 // 10 = 1 (carry)
            # example 7  // 10 = 0
            # [KEY] this effectively handles the carry-over elegantly
            _sum //= 10

            if cur1:
                _sum += cur1.val
                cur1 = cur1.next

            if cur2:
                _sum += cur2.val
                cur2 = cur2.next

            # modulous division
            # example 14 % 10 = 4
            cur.next = ListNode(_sum % 10)
            cur = cur.next

        # when the last digit sum requires carry over
        if _sum >= 10:
            cur.next = ListNode(1)

        return dummy.next

# [KEY] use of dummy node, modulous, integer division
# use accumulator _sum to stack values in

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
