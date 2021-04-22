class Node:
    def __init__(self):
        self.dic = {}
        self.is_last = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for x in word:
            cur.dic[x] = cur.dic.get(x) or Node()
            cur = cur.dic.get(x)

        cur.is_last = True

    def _traverse(self, word):
        cur = self.root

        for x in word:
            if cur is None:
                return None
            cur = cur.dic.get(x)

        return cur

    def search(self, word):
        node = self._traverse(word)

        return node and node.is_last

    def starts_with(self, prefix):
        return self._traverse(prefix)
