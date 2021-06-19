class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for entry in cpdomains:
            count, string = entry.split()
            words = string.split('.')
            j, tmp = len(words) - 1, []
            while j >= 0:
                tmp += [words[j]]
                key = '.'.join(tmp[::-1])
                dic[key] = dic.get(key, 0) + int(count)
                j -= 1

        res = []
        for sub_domain, count in dic.items():
            entry = str(count) + ' ' + sub_domain
            res.append(entry)

        return res
