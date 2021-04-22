class Solution:
    # [KEY] process the previous number when hitting the current sign
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []

        for c in s:
            if (c == ' '):
                continue

            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num
                # after using 'sign' and 'num', reset them
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                # resetting 'res' to perform in-paren calculation
                res = 0
            elif c == ')':
                # perform in-paren calculation
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        # handle the last number cuz' there is no sign after the last number
        res += sign * num

        return res
