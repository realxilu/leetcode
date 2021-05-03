class Solution:
    def calculate(self, s):
        res = 0
        stack = []
        sign, num = 1, 0

        for c in s:
            # ignore space
            if (c == ' '):
                continue

            if c.isdigit():
                # [TRICK] build the number using digits
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num # this is for the previous* operation
                # the reset is for the next operation
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                # save the current 'res' and 'sign' into stack
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                # in-paren calculation
                res += sign * num
                num = 0
                res *= stack.pop() # sign
                res += stack.pop() # res

        # [ATTENTION] handle the last number cuz' there is no sign after the last number
        res += sign * num

        return res

 # [KEY] 1 + 2 - 3
 # whenever an operator is hit, it means a number must have been formed.
 # res += sign * num is for the prevoius operation
 # what is the previous operation when the first '+' was hit, it is res = 0 (init) + 1
