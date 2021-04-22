from heapq import *


class Solution:
    def merge_k_lists(self, lists):
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(heap)

        cur = dummy = ListNode(-1)
        while heap:
            # Note: tie-breaker: 'i' guarantees uniqueness
            _, i, node = heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
