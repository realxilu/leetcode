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
            # 'not stack' covers test case 1
            elif not stack or stack.pop() != x:
                return False

        return len(stack) == 0


# Note we don't need hashmap here, just push the closing paren into the stack
# TEST CASES:
# 1. ))))
# [] -> the stack is empty prematurely, the stack shouldn't be empty at this point, return false
# 2. ()) 
# [)] -> [] -> the stack is empty again like case 1
# 3. (((
#  [)] -> [)] -> [)], len(stack) is 3 in the end, return false
# 4. (()
# [)] -> [))] -> [)], len(stack) is 1 in the end, return false
# 5. (()())
# [)] -> [))] -> [)] -> [))] -> [)] -> [], len(stack) is 0 in the end, return true
