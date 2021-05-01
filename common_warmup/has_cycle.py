# https: // leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while True:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
