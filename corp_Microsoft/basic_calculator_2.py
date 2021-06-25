class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        # [TRICK] add a '+' at the end
        s = s.strip() + '+'
        stack, sign, tmp = [], '+', 0

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                tmp = 10 * tmp + int(c)
            else:
                if sign == '+':
                    stack.append(tmp)
                if sign == '-':
                    stack.append(-tmp)
                if sign == '*':
                    stack.append(stack.pop() * tmp)
                if sign == '/':
                    top = stack.pop()
                    # top // tmp will floor the number which is problematic for negative divisions
                    if top // tmp < 0 and top % tmp != 0:
                        # if the divison is negative and not a whole division, to need to move the number to the right by 1 unit
                        stack.append(top // tmp + 1)
                    else:
                        stack.append(top // tmp)

                sign, tmp = c, 0

        return sum(stack)
