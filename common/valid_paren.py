class Solution:
    def isValid(self, s):
        stack = []
        for x in s:
            if x == '(':
                stack.append(')')
            elif x == '[':
                stack.append(']')
            elif x == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop() != x:
                return False

        return len(stack) == 0
