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
        
        self.head = Node(-1, -1)  # senitenial
        self.tail = Node(-1, -1)  # senitenial
        # setup head and tail's relationshiop
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
        # remove-add is what guarentees LRU property
        if k in self.dic:
            self._remove(self.dic[k])

        # add first then think about eviciting
        new_node = Node(k, v)
        self._add(new_node)
        self.dic[k] = new_node

        # evict if over capacity
        if len(self.dic) > self.capacity:
            # evict items from the head, insert from behind
            head_next = self.head.next
            self._remove(head_next)
            del self.dic[head_next.k]

    # node passed in as a reference for both helper function 
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
