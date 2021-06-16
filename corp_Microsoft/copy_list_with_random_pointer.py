class Solution:
    def copyRandomList(self, head):
        dic = {} #hashmap in python

        # 1st traversal creates a mapping
        cur = head
        while cur:
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next

        # 2nd traversal sets up the proper relationship between nodes
        cur = head
        while cur:
            # dic.get('stuff') is safer than dic['stuff']
            dic.get(cur).next = dic.get(cur.next)
            dic.get(cur).random = dic.get(cur.random)
            cur = cur.next

        return dic.get(head)

# [KEY] similar to clone_graph.py

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
