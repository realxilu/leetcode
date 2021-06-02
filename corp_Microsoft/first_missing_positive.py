class Solution:
    # O(nlogn)
    def firstMissingPositive(self, A):
        # write your code in Python 3.6
        s = set()
        for x in A:
            if x > 0:
                s.add(x)

        i = 0
        for i, x in enumerate(sorted(list(s))):
            if x - i > 1:
                return i + 1

        return x + 1 if x > 0 else 1

# [KEY] don't be lazy, diagram it out. sometimes it is hard to think inside your head without viz
# Once I wrote out the indices and numbers, the relationship between x and i became much claerer.