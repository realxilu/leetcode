from collections import deque
class Solution:
    def ladderLength(self, begin_word, end_word, word_list):
        word_set = set(word_list)
        alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]

        q = deque([(begin_word, 1)])
        while q:
            cur_word, level = q.popleft()
            if cur_word == end_word:
                return level

            # examine each word and replace the ith word with either of the 26 chars and check if the new word is in the set
            for i in range(len(cur_word)):
                for c in alpha:
                    # [:i] can't reach 'i', c is at ith position, cur_word goes from i + 1 to the end
                    next_word = cur_word[:i] + c + cur_word[i + 1:]
                    # this method is cool, cuz the next_word might not 
                    if next_word in word_set:
                        word_set.remove(next_word)  # mark as visited
                        q.append((next_word, level + 1))

        return 0
#[KEY][BFS]
