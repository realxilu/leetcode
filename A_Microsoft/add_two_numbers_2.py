class Solution:
    def add_two_numbers(self, l1, l2):
        arr1, arr2 = [], []
        cur = l1
        while cur:
            arr1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            arr2.append(cur.val)
            cur = cur.next

        sum_, list_ = 0, []
        while len(arr1) or len(arr2):
            sum_ //= 10
            if len(arr1):
                sum_ += arr1.pop() or 0
            if len(arr2):
                sum_ += arr2.pop() or 0
            list_.append(sum_ % 10)
        if sum_ >= 10:
            list_.append(1)

        cur = dummy = ListNode(-1)
        while len(list_):
            cur.next = ListNode(list_.pop())
            cur = cur.next

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
