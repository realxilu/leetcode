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
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, k):
        if k in self.dic:
            node = self.dic[k]
            self._remove(node)
            self._add(node)

            return node.v

        return -1

    def put(self, k, v):
        if k in self.dic:
            self._remove(self.dic[k])

        node = Node(k, v)
        self._add(node)
        self.dic[k] = node

        if len(self.dic) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dic[node.k]

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
