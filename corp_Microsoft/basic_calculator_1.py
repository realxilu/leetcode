class Solution:
    def calculate(self, s):
        if not s:
            return None

        s += '+'  # given how the algorithm works, we only do calculation after seeing a sign
        res, stack, sign, num = 0, [], 1, 0

        for c in s:
            if (c == ' '):
                continue

            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num  # this is for the previous operation
                # reset for next op
                num, sign = 0, 1
            elif c == '-':
                res += sign * num
                num, sign = 0, -1
            elif c == '(':
                # save the current 'res' and 'sign' into stack
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ')':
                # in-paren calculation
                res += sign * num
                num = 0
                res *= stack.pop()  # sign
                res += stack.pop()  # res

        return res

 # [KEY] 1 + (2 - 3)
 # whenever an operator is hit, it means a number must have been formed.
 # res += sign * num is for the prevoius operation
 # what is the previous operation when the first '+' was hit, it is res = 0 (init) + 1
 # NOTE this is different from calculator 2, we don't dump everything into stack, the central idea is to construct an accumulator
