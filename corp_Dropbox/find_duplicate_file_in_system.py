from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        if not paths:
            return paths

        dic = defaultdict(list)
        for x in paths:
            l = x.split()
            path, file_list = l[0], l[1:]

            for x in file_list:
                [name, content] = self._get_file_name(x)
                dic[content].append(path + '/' + name)

        return [val for val in dic.values() if len(val) > 1]

    # [file_name, file_content]
    def _get_file_name(self, name_content):
        index1 = name_content.find('(')
        index2 = name_content.find(')')

        file_name = name_content[:index1]
        file_content = name_content[index1 + 1:index2]

        return [file_name, file_content]

# [KEY] This is my solution. Very proud that I can solve it myself.
# The key is to draw a hashmap that stores the intended content.