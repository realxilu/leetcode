class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # this creats a new list, there are two linkedlist instead of one
        head2 = self.reverse_list(slow)
        cur1, cur2 = head, head2
        while True:
            if cur1 is slow:
                break

            if cur1.val != cur2.val:
                return False

            cur1, cur2 = cur1.next, cur2.next

        return True

    # note this is not in-place
    def reverse_list(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverse_list(head.next)
        head.next.next = head
        head.next = None

        return new_head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [TWO_POINTER] O(N) time O(1) space
