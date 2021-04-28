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
   
# TODO refactor
# const isValid = (string) = > {
#     let stack = []
#     // define parentheses pairs
#     let dict = {
#         '{': '}',
#         '[': ']',
#         '(': ')',
#     }

#     for (let c of string) {
#         if (c == = '{' | | c == = '[' | | c == = '(')
#           stack.push(c)
#         else if (c !== dict[stack[stack.length - 1]])
#           return false
#         else
#           stack.pop()
#     }

#     return stack.length === 0
# }
