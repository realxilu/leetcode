from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create data structures + the in_degree of each unique letter to 0
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # build graph and indegree
        for word1, word2 in zip(words, words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in adj_list[char1]:
                        adj_list[char1].add(char2)
                        in_degree[char2] += 1
                    break
            # [PY] for-else
            else:  # check that the second word isn't a prefix of first word
                if len(word2) < len(word1):
                    return ''

        # core idea: repeatedly pick off nodes with indegrees of 0
        # [bfs] source init: for nodes whose indegrees are zero
        source, q = [], deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            c = q.popleft()
            source.append(c)
            # check current node's neighbors
            for d in adj_list[c]:
                # deduct indegrees of current node's neighbors
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    q.append(d)

        # if not all letters are in source, that means there was a cycle (not DAG)
        # therefore there is no valid toposort. Return '' as required
        if len(source) < len(in_degree):
            return ''
        # join strings as required
        return ''.join(source)
