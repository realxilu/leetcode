class Solution:
    def findCelebrity(self, n):
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i

        if any(knows(candidate, i) for i in range(candidate)):
            return -1

        if any(not knows(i, candidate) for i in range(n)):
            return -1

        return candidate

# [KEY] Observe important properties. Naming is also important to solving this problem. 
# [Definition] a celebrity is defined as a person that doesn't know anyone but anyone knows the celebrity
# The first for-loop is the most crucial part to solving the problem
# Initialize the candidate to 0 if candidate knows 'i' then the currrent assumed candidate cannot be celebrity and i _might_ be a celebrity

# Time complexity = O(n), 'any' function scans through the array left to right under the hood
# Space complexity = O(1) no extra data structure
