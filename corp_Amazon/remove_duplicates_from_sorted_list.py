class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next

        return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
