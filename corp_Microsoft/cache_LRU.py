class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        
        self.head = Node(-1, -1)  # head dummy
        self.tail = Node(-1, -1)  # tail dummy
        # link head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, k):
        if k in self.dic:
            node = self.dic[k]
            # this will remove the referenced node from middle
            self._remove(node)
            # this will insert the referenced node from the back
            self._add(node)

            return node.v

        return -1 # if not found

    def put(self, k, v):
        # remove-add paradigm is what guarentees LRU property
        if k in self.dic:
            self._remove(self.dic[k])

        new_node = Node(k, v)
        self._add(new_node)
        self.dic[k] = new_node

        # if over capacity, remove head since we insert from behind
        if len(self.dic) > self.capacity:
            head_next = self.head.next
            self._remove(head_next)
            del self.dic[head_next.k]

    # pass in reference for a node and remove it from the linkedlist 
    def _remove(self, node):
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        _next.prev = _prev

    # node insertion happens from behind
    def _add(self, node):
        _prev = self.tail.prev
        _prev.next = node
        self.tail.prev = node
        node.prev = _prev
        node.next = self.tail
# [KEY] \images\lru.JPG
# 1) use two dummy nodes 2) use two helper functions
