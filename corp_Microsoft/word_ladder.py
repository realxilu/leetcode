from collections import deque


class Solution:
    def ladder_length(self, begin_word, end_word, word_list):
        word_set = set(word_list)
        alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]

        q = deque([(begin_word, 1)])
        while q:
            cur_word, level = q.popleft()
            if cur_word == end_word:
                return level

            for i in range(len(cur_word)):
                for c in alpha:
                    next_word = cur_word[:i] + c + cur_word[i + 1:]
                    if next_word in word_set:
                        word_set.remove(next_word)  # mark as visited
                        q.append((next_word, level + 1))

        return 0
