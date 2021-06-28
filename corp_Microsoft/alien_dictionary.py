from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create data structures + the in_degree of each unique letter to 0
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # populate adj_list and in_degree
        # watch how to process first and second word
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            # [PY] for-else loop
            else:  # Check that the second word isn't a prefix of first word
                if len(second_word) < len(first_word):
                    return ''

        # repeatedly pick off nodes with indegrees of 0
        source = []
        # source init: for nodes whose indegrees are zero
        q = deque([c for c in in_degree if in_degree[c] == 0])
        # bfs
        while q:
            c = q.popleft()
            source.append(c)
            # check current node's neighbors
            for d in adj_list[c]:
                # deduct indegrees of current node's neighbors
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    q.append(d)

        # if not all letters are in source, that means there was a cycle
        # therefore there is no valid toposort. Return '' as required
        if len(source) < len(in_degree):
            return ''
        # join strings as required
        return ''.join(source)
