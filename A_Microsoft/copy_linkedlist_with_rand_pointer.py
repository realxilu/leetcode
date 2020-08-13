class Solution:
    def copy_random_list(self, head):
        dic = {}
        m = n = head

        # first traversal creates a mapping
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next

        # second traversal sets up the proper relationship between nodes
        while n:
            dic.get(n).next = dic.get(n.next)
            dic.get(n).random = dic.get(n.random)
            n = n.next

        return dic.get(head)


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
