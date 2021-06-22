class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    reverse_adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ''

        # Step 2: dfs
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ''

        return ''.join(output) 