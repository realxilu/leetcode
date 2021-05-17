import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [['']]

        dic = collections.defaultdict(list)
        for word in strs:
            dic[str(sorted(word))].append(word)

        res = []
        for val in dic.values():
            res.append(val)

        return res
