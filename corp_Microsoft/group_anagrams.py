from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None

        dic = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            dic[sorted_word].append(word)

        return list(dic.values())
