class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        cur, s = headA, set()
        while cur:
            s.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in s:
                return cur
            cur = cur.next

        return None
