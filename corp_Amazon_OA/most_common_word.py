import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub('\W+', ' ', paragraph).strip()
        dic, _max, my_word = {}, 0, None

        for word in paragraph.lower().split():
            if word in banned:
                continue

            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

            if dic[word] > _max:
                _max = dic[word]
                my_word = word

        return my_word
