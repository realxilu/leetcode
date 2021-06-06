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
        self.head = Node(-1, -1)  # dummy
        self.tail = Node(-1, -1)  # also dummy
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, k):
        if k in self.dic:
            node = self.dic[k]
            self._remove(node)
            self._add(node)

            return node.v

        return -1 # per spec

    def put(self, k, v):
        if k in self.dic:
            self._remove(self.dic[k])

        new_node = Node(k, v)
        self._add(new_node)
        self.dic[k] = new_node

        # evict if length is great than 1
        if len(self.dic) > self.capacity:
            head_next = self.head.next
            self._remove(head_next)
            del self.dic[head_next.k]

    def _remove(self, node):
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        _next.prev = _prev

    def _add(self, node):
        _prev = self.tail.prev
        _prev.next = node
        self.tail.prev = node
        node.prev = _prev
        node.next = self.tail

# [KEY] \images\lru.JPG
