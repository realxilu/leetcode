class Solution:
    def addTwoNumbers(self, l1, l2):
        cur1, cur2 = l1, l2
        # sentinel/dummy node
        cur = dummy = ListNode(-1)
        _sum = 0

        while cur1 or cur2:
            # [TRICK] this effectively handles the carry-over elegantly
            # example 14 // 10 = 1 (carry case)
            # example 7  // 10 = 0 (normal case)
            _sum //= 10

            if cur1:
                _sum += cur1.val
                cur1 = cur1.next

            if cur2:
                _sum += cur2.val
                cur2 = cur2.next

            # modulous division used to extract the least significant digit
            # example 14 % 10 = 4
            cur.next = ListNode(_sum % 10)
            cur = cur.next

        # when the last digit sum requires carry over
        if _sum >= 10:
            cur.next = ListNode(1)

        return dummy.next

# [KEY] use of dummy node, modulous, integer division
# use accumulator _sum to stack values in. Then reset _sum using _sum//=10

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
