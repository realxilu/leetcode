# https: // leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        
        cur.is_word = True

    def search(self, word):
        cur = self.root
        for c in word:
            cur = cur.children.get(c)
            if cur is None:
                return False
        
        return cur.is_word

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return False
        
        return True

# [KEY] collections.defaultdict(TrieNode)
# defaultdict vs {} if the search value is not found, the default value will be used
