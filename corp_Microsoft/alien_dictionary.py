from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create data structures + the in_degree of each unique letter to 0
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # We need to populate adj_list and in_degree
        # watch how to process first and second word
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word
                if len(second_word) < len(first_word):
                    return ''

        # We need to repeatedly pick off nodes with an indegree of 0
        source = []
        q = deque([c for c in in_degree if in_degree[c] == 0])
        # BFS structure
        while q:
            c = q.popleft()
            source.append(c)
            # check the neighbors
            for d in adj_list[c]:
                # deduct indegrees of c's neighbors
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    q.append(d)

        # If not all letters are in source, that means there was a cycle and so
        # no valid ordering. Return '' as per the problem description
        if len(source) < len(in_degree):
            return ''
        # Otherwise, convert the ordering we found into a string and return it
        return ''.join(source)

# for...else loop

# bfs structure
# while q:
#     node = q.popleft()
#     print(node)
#     for nb in node.neighbors
#         q.append(nb)