class Solution:
    def findCelebrity(self, n):
        candidate = 0

        for i in range(n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            # 'i != candidate' is important since the candidate can know itself (given how the graph is given)
            if i != candidate and knows(candidate, i):
                return -1

            # if there is an average joe that doesn't know the candidate then it is not celeb
            if not knows(i, candidate):
                return -1

        return candidate

# [KEY] Observe important properties. Naming is also important to solving this problem.
# [Definition] a celebrity is defined as a person that doesn't know anyone but anyone knows the celebrity
# The first for-loop is the most crucial part to solving the problem
# Initialize the candidate to 0 if candidate knows 'i' then the currrent assumed candidate cannot be celebrity and i _might_ be a celebrity

# Time complexity = O(n), 'any' function scans through the array left to right under the hood
# Space complexity = O(1) no extra data structure
