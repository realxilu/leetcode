import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        
        return self.res

    def dfs(self, node, word):
        # the word has finally been shrunk to zero length
        if not word and node.isWord:
            self.res = True
            return

        # if '.' then it is automatically a match, go check the next sub word
        if word[0] == '.':
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            
            if not node:
                return

            self.dfs(node, word[1:])

# Trie is a tree-like structure. Each node of trie contains a hashmap/dict.